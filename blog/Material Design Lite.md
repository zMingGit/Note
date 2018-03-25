

# Material Design Lite



这是一个Google的css框架， 用法类似于Bootstrap，但是两者的设计有一点区别. 在我看来Bootstrap的设计更加硬派，有种商务化的感觉，而Material design lite给我感觉更圆润，更有设计的空间.



## 博客历史

在刚上大学的时候，那时候看着很多大牛都在博客园或者其他类似的站上写博客，我也就跟风的在博客园上写，但是没坚持多久，就差不多荒废了，而且写出来的文章都是条例不清晰，自己都不明白自己在讲些什么 (现在也差不多.



之后一段时间偶然看到了hugo， 静态博客的一个框架， 发现这里的几个主题特别好看，随后就用hugo建立了博客，然后挂在github page上面. 但是也想过自己弄个服务器来维护，但是当时没啥钱，而且觉得用github page来托管更省事。



然后，看到了hexo(也是一个静态博客的框架)，发现hexo里面的主题更简洁，更符合我对于博客的期望，所以就又迁移到了hexo.



之后学习了Django, 就想做点东西，所以博客成了django + bootstrap来主导，用uwsgi和nginx通信，挂在某[vultr](http://vultr.com)上，页面的设计也是基于hexo的某个主题，也算是利用了一些css3的特性，当时感觉看起来还行。



最后就是现在了，看到了[他](https://blog.viosey.com/)的博客，发现这也是个hexo的主题，麻木了，继续迁移吧。仔细看了下，发现这个主题是依赖于Google的[Material Deisgn](https://material.io/), 然后就直奔主题，看google的文档去了，随后发现了google考虑的还是非常全面的，直接给了一个[博客的样例](https://getmdl.io/templates/index.html)，所以毫无悬念的就抄了过来，然后就成了现在的博客.



在最后这次迁移的期间，忽然看到[一个博客](https://ekyu.moe/), 看到左下角那个动漫人物的第一眼我就呆住了，这么逼真，想都不想，开始抄吧。 但是这个东西看页面源码一时间没看出啥来，然后在Telegram上问了一下大佬，给了个答案,这是live2d做的，随后找到了[live2djs的hexo插件](https://github.com/EYHN/hexo-helper-live2d)以及[类似的项目](https://github.com/xiazeyu/live2d-widget.js)。但是我比较笨，也比较懒，开始不想在去弄hexo了，就想跟着那个类似的项目的文档去做出来就好了，但是也许还是我比较笨，没看明白，折腾了几个晚上，最后还是抄的hexo插件.



## 总结



虽然标题是google的产品，但是压根没说到这个, 光顾着说历史了。但是有个经验非常重要，大部分想要的东西，基本上网上都有了，只要去找就是了，就算没有，那也肯定是有人正在开发中，所以等一段时间抄就是了.