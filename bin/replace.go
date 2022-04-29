// replace -- in-place edit a post
// usage: replace [old string] [new string]

package main

import (
	"fmt"
	"log"
	"os"
	"strings"
)

const dir = "pages/blog/"

func main() {
	if len(os.Args) != 3 {
		fmt.Println("usage: replace [old string] [new string]")
		os.Exit(1)
	}

	oldStr, newStr := os.Args[1], os.Args[2]

	posts, err := os.ReadDir(dir)
	if err != nil {
		log.Fatalln(err)
	}
	for _, p := range posts {
		path := dir + p.Name()
		input, err := os.ReadFile(path)
		if err != nil {
			log.Fatalln(err)
		}

		lines := strings.Split(string(input), "\n")
		for i, line := range lines {
			if strings.Contains(line, oldStr) {
				line = strings.ReplaceAll(line, oldStr, newStr)
				lines[i] = line
			}
		}
		output := strings.Join(lines, "\n")
		err = os.WriteFile(path, []byte(output), 644)
		if err != nil {
			log.Fatalln(err)
		}
	}
}
