---
template:
slug: go-shell-prompt
title: Writing a shell prompt in Go
subtitle: Kinda faster than bash
date: 2021-08-12
---

For context, my bash prompt was previously [written in, well,
bash](https://git.icyphox.sh/dotfiles/tree/bash/.bashrc.d/99-prompt.bash?id=d7b391845abc7e97f2b1b96c34b4b1789b2ab541).
It used to call out to `git` for getting the branch and worktree status
info. Parsing the output of `git status` and all that. It was ok, but I
wanted something ... cleaner.

I chose Go, despite having written
[nicy](https://github.com/icyphox/nicy) in Nim[^1]; I'm in a Go-phase right
now, just like I was in a Nim-phase back in 2018. Anyway, let's cut to
the chase.

[^1]: It's a prompt "framework" thing that I actually only used for a
      month or so.

## the basics

The current working directory is the bare minimum in a prompt. I prefer
having it shortened; for example: `/home/icy/docs/books/foo.epub` →
`~/d/b/foo.epub`. Let's write a function `trimPath` to do this for us:

```go
// Truncates the current working directory:
//   /home/icy/foo/bar -> ~/f/bar
func trimPath(cwd, home string) string {
	var path string
	if strings.HasPrefix(cwd, home) {
		path = "~" + strings.TrimPrefix(cwd, home)
	} else {
		// If path doesn't contain $HOME, return the
		// entire path as is.
		path = cwd
		return path
	}
	items := strings.Split(path, "/")
	truncItems := []string{}
	for i, item := range items {
		if i == (len(items) - 1) {
			truncItems = append(truncItems, item)
			break
		}
		truncItems = append(truncItems, item[:1])
	}
	return filepath.Join(truncItems...)
}
```

`trimPath` takes two args: the current working directory `cwd`, and the
home directory `home`. We first check if `cwd` starts with `home`, i.e.
we're in a subdirectory of `home`; if yes, trim `home` from `cwd`, and
replace it with a tilde `~`. We now have `~/docs/books/foo.epub`.

Also note that we return the path as-is if we're not in a subdir of
`home` -- i.e. paths under `/`, like `/usr`, etc. I like to see these
completely, just to be sure.

We then split the path at `/`[^2], and truncate each item in the
resulting list -- except for the last -- down to the first character.
Join it all together and return the resulting string -- we have
`~/d/b/foo.epub`.

[^2]: I don't care about Windows.

Next up: color.

```go
var (
	red   = color("\033[31m%s\033[0m")
	green = color("\033[32m%s\033[0m")
	cyan  = color("\033[36m%s\033[0m")
)

func color(s string) func(...interface{}) string {
	return func(args ...interface{}) string {
		return fmt.Sprintf(s, fmt.Sprint(args...))
	}
}
```
... I'll just let you figure this one out.

## git branch and clean/dirty info

The defacto lib for git in Go is often
[go-git](https://github.com/go-git/go-git). I don't disagree that it is
a good library: clean APIs, good docs. It just has one huge issue, and
especially so in our case. It's `worktree.Status()` function -- used to
fetch the worktree status -- is [awfully
slow](https://github.com/go-git/go-git/issues/327). It's not noticeable
in small repositories, but even relatively large ones (~30MB) tend to
take about 20 seconds. That's super not ideal for a prompt.[^3]

[^3]: https://git.icyphox.sh/dotfiles/commit/?id=e1f6aaaf6ffd35224b5d3f057c28fb2560e1c3b0

The alternative? [libgit2/git2go](https://github.com/libgit2/git2go), of
course! It's the Go bindings for libgit2 -- obviously, it requires CGo,
but who cares.

First things first, let's write `getGitDir` to find `.git` (indicating
that it's a git repo), and return the repository path. We'll need this
to use git2go's `OpenRepository()`.

```go
// Recursively traverse up until we find .git
// and return the git repo path.
func getGitDir() string {
	cwd, _ := os.Getwd()
	for {
		dirs, _ := os.ReadDir(cwd)
		for _, d := range dirs {
			if ".git" == d.Name() {
				return cwd
			} else if cwd == "/" {
				return ""
			}
		}
		cwd = filepath.Dir(cwd)
	}
}
```

This traverses up parent directories until it finds `.git`, else,
returns an empty string if we've reached `/`. For example: if you're in
`~/code/foo/bar`, and the git repo root is at `~/code/foo/.git`, this
function will find it.

Alright, let's quickly write two more functions to return the git branch
name, and the repository status -- i.e., dirty or clean.

```go
// Returns the current git branch or current ref sha.
func gitBranch(repo *git.Repository) string {
	ref, _ := repo.Head()
	if ref.IsBranch() {
		name, _ := ref.Branch().Name()
		return name
	} else {
		return ref.Target().String()[:7]
	}
}
```

This takes a `*git.Repository`, where `git` is `git2go`. We first get
the `git.Reference` and check whether it's a branch. If yes, return the
name of the branch, else -- like in the case of a detached HEAD state --
we just return a short hash.

```go
// Returns • if clean, else ×.
func gitStatus(repo *git.Repository) string {
	sl, _ := repo.StatusList(&git.StatusOptions{
		Show:  git.StatusShowIndexAndWorkdir,
		Flags: git.StatusOptIncludeUntracked,
	})
	n, _ := sl.EntryCount()
	if n != 0 {
		return red("×")
	} else {
		return green("•")
	}
}
```

We use the
[`StatusList`](https://godocs.io/github.com/libgit2/git2go/v31#Repository.StatusList)
function to produce a `StatusList` object. We then check the
`EntryCount`, i.e., the number of modified/untracked/etc. files
contained in `StatusList`.[^4] If this number is 0, our repo is clean;
dirty otherwise. Colored symbols are returned accordingly.

[^4]: This took me a lot of going back and forth, and reading
      https://libgit2.org/libgit2/ex/HEAD/status.html to figure out.

## putting it all together

Home stretch. Let's write `makePrompt` to make our prompt.

```go
const (
	promptSym = "▲"
)

func makePrompt() string {
	cwd, _ := os.Getwd()
	home := os.Getenv("HOME")
	gitDir := getGitDir()
	if len(gitDir) > 0 {
		repo, _ := git.OpenRepository(getGitDir())
		return fmt.Sprintf(
			"\n%s (%s %s)\n%s",
			cyan(trimPath(cwd, home)),
			gitBranch(repo),
			gitStatus(repo),
			promptSym,
		)
	}
	return fmt.Sprintf(
		"\n%s\n%s",
		cyan(trimPath(cwd, home)),
		promptSym,
	)
}

func main() {
	fmt.Println(makePrompt())
}
```

There isn't much going on here. Get the necessary pieces like the
current working directory, home and the git repo path. We return the
formatted prompt string according to whether we're in git or not.

Setting the prompt is simple. Point `PS1` to the built binary:

```bash
PS1='$(~/dotfiles/prompt/prompt) '
```

And here's what it looks like, rendered:
![go prompt](https://cdn.icyphox.sh/boh7u.png)

## benchmarking

Both "benchmarks" were run inside a sufficiently large git repository,
deep inside many subdirs.

To time the old bash prompt, I just copied all the bash functions,
pasted it in my shell and ran:

```shell
~/C/d/a/n/y/b/d/t/yaml-1.1 (master •)
▲ time echo -e "\n$(prompt_pwd)$(git_branch)\n▲$(rootornot)"

# output
~/C/d/a/n/y/b/d/t/yaml-1.1 (master •)
▲

real    0m0.125s
user    0m0.046s
sys     0m0.079s

```

0.125s. Not too bad. Let's see how long our Go prompt takes.

```shell
~/C/d/a/n/y/b/d/t/yaml-1.1 (master •)
▲ time ~/dotfiles/prompt/prompt

# output
~/C/d/a/n/y/b/d/t/yaml-1.1 (master •)
▲

real    0m0.074s
user    0m0.031s
sys     0m0.041s

```

0.074s! That's pretty fast. I ran these tests a few more times, and the
bash version was consistently slower -- averaging ~0.120s; the Go
version averaging ~0.70s. That's a win.

You can find the entire source [here](https://git.icyphox.sh/dotfiles/tree/prompt).
