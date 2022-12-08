# Client Renderer
Allows you to define which class will render the output. Default is a text renderer, but a number of the clients have their own renderers to support Rich Media objects defined in AIML 2.1

```yaml
console:
  renderer: programy.clients.render.text.TextRenderer
```

* **renderer** - Python class to render text