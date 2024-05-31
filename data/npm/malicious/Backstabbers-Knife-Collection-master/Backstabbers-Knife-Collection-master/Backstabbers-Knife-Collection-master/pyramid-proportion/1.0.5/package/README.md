# jquery-pyramid-proportion.js

[![npm version](https://badge.fury.io/js/pyramid-proportion.svg)](https://badge.fury.io/js/pyramid-proportion)

一个基于jquery的金字塔图，可根据传入比例显示各层高度[jquery-pyramid-proportion.js (jQuery version)](https://github.com/kwen8/jquery-pyramid-proportion.js).

### Usage

```html
<body>
<div class="pyramid"></div>

<!-- at the end of the body -->
<script src="jquery.min.js"></script>
<script type="text/javascript" src="jquery-pyramid-proportion.js"></script>
<script type="text/javascript">
    $(".pyramid").pyramid({
        proportion: [10,20,30]
    });
</script>
</body>
```

### Options
```js
{
    proportion: [10,30,50], //传入的每层比例
}
```

### Install
You can copy and include any of the following file:

* [lib/jquery-pyramid-proportion.js](https://raw.githubusercontent.com/kwen8/pyramid-proportion/master/lib/jquery-pyramid-proportion.js) ~ 2kb
* [lib/jquery-pyramid-proportion.min.js](https://raw.githubusercontent.com/kwen8/pyramid-proportion/master/lib/jquery-pyramid-proportion.min.js) ~ 1kb

#### NPM

Also available on npm https://www.npmjs.com/package/pyramid-proportion

```
npm install pyramid-proportion
```

### Credits

Original library: [jquery-pyramid-proportion.js](https://github.com/kwen8/pyramid-proportion)

### License

MIT License
