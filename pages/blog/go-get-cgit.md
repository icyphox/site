---
template:
slug: go-get-cgit
title: Make cgit go gettable
subtitle: go get git.icyphox.sh/* works!
date: 2021-07-14
---

`go get` requires the presence of the `go-import` meta tag[^1] on the
repository's web page. cgit doesn't support it out of the box; instead,
we can make nginx inject it into every page. Enter: `sub_filter`.[^2]

`sub_filter` is a function that simply performs a string replace. For
example:
```nginx
location / {
  sub_filter '<img src=dog.png>' '<img src=cat.png>';
  sub_filter_once on;
}
```

In our case, we want to have the meta tag injected inside `<head>`.

```nginx
server {
  listen 443 ssl;
  server_name git.icyphox.sh;

  location / {
    ...

    sub_filter '</head>'
      '<meta name="go-import" content="$host$uri git https://$host$uri"></head>';
    sub_filter_once on;
  }
}
```

The closing `</head>` tag gets replaced -- injecting the meta tag inside
`<head>`. This can also be extended to add the `go-source` meta tag as
well.

[^1]: https://godocs.io/cmd/go#hdr-Remote_import_paths
[^2]: http://nginx.org/en/docs/http/ngx_http_sub_module.html
