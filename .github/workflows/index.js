const YAML = require('yamljs');
const fs = require('fs');

// اقرأ ملف YAML
const content = fs.readFileSync('_config.yml', 'utf8');

// تحويل الملف إلى كائن JavaScript
const data = YAML.parse(content);

console.log(data);
const favicon = data.favicon;
const title = data.title;
const description = data.description;

// استخدم البيانات في موقعك
document.querySelector('link[rel="icon"]').setAttribute('href', favicon);
document.title = title;
document.querySelector('meta[name="description"]').setAttribute('content', description);
