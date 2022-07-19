# MD Buttons

Add nice SVG buttons to your Markdown files 🎨

<p align="center">
    <a href="#how-does-it-work">
        <img src="https://md-btn.deta.dev/button.svg?text=Awesome%20%F0%9F%9A%80%20Tell%20me%20more!&w=250&px=40&py=40" alt="Awesome! Tell me more!">
    </a>
</p>

## How does it work?

1. Build your button URL:

[https://md-btn.deta.dev/button.svg?text=Hello%20World](https://md-btn.deta.dev/button.svg?text=Hello%20World)

2. Add it to your Markdown content as an image:

```md
![Hello world](https://md-btn.deta.dev/button.svg?text=Hello%20World)
```

3. Enjoy!

![Hello world](https://md-btn.deta.dev/button.svg?text=Hello%20World)

## Examples

### Width (`w`)

```md
![](https://md-btn.deta.dev/button.svg?text=Hello%20World&w=300)
```

![](https://md-btn.deta.dev/button.svg?text=Hello%20World&w=300)

### Font size (`fs`)

By default, the font size will be automatically guessed so that the text fits within the desired width. You can however force a specific size, but in this case the text may overflow the background.

```md
![](https://md-btn.deta.dev/button.svg?text=Hello%20World&fs=48)
```

![](https://md-btn.deta.dev/button.svg?text=Hello%20World&fs=48)

### Background color (`bg`)

```md
![](https://md-btn.deta.dev/button.svg?text=Hello%20World&bg=e74c3c)
```

![](https://md-btn.deta.dev/button.svg?text=Hello%20World&bg=e74c3c)

### Text color (`fg`)

```md
![](https://md-btn.deta.dev/button.svg?text=Hello%20World&fg=e74c3c)
```

![](https://md-btn.deta.dev/button.svg?text=Hello%20World&fg=e74c3c)

### Padding (`px` and `py`)

```md
![](https://md-btn.deta.dev/button.svg?text=Hello%20World&px=50)
```

![](https://md-btn.deta.dev/button.svg?text=Hello%20World&px=50)

```md
![](https://md-btn.deta.dev/button.svg?text=Hello%20World&py=50)
```

![](https://md-btn.deta.dev/button.svg?text=Hello%20World&py=50)

### Border radius (`br`)

```md
![](https://md-btn.deta.dev/button.svg?text=Hello%20World&br=0)
```

![](https://md-btn.deta.dev/button.svg?text=Hello%20World&br=0)

## License

MIT
