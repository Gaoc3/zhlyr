
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Markdown to HTML Converter</title>
<script src="https://cdn.jsdelivr.net/npm/remarkable/dist/remarkable.min.js"></script>
</head>
<body>

<h2>أدخل النص Markdown:</h2>
<textarea id="markdown-input" rows="10" cols="50"># عنوان
هذا نص **Markdown** يمكن تحويله إلى HTML.
</textarea>
<br>
<button onclick="convertMarkdown()">تحويل إلى HTML</button>

<h2>النص المحول إلى HTML:</h2>
<div id="html-output"></div>

<script>
function convertMarkdown() {
    var markdownInput = document.getElementById('markdown-input').value;
    var md = new Remarkable();
    var htmlOutput = md.render(markdownInput);
    document.getElementById('html-output').innerHTML = htmlOutput;
}
</script>

</body>
</html>


## Code Area :
- **Install zhlyr:**
```bash
pip install zhlyr
```

## what is zhlyr?
  - **A platform aimed at music enthusiasts, providing tools for managing and discovering music, fetching song lyrics, and utilizing machine learning algorithms to predict the name of a song from a short audio snippet.**











## My Social Media Links Accounts
- [GitHub](https://github.com/) [<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="20" height="20">](https://github.com/)
- [Instagram](https://www.instagram.com/) [<img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" alt="Instagram" width="20" height="20">](https://www.instagram.com/)
- [Telegram](https://web.telegram.org/) [<img src="https://cdn-icons-png.flaticon.com/512/2111/2111646.png" alt="Telegram" width="20" height="20">](https://web.telegram.org/)


<span style="color: red;">بحب طيز السيسي</span>

