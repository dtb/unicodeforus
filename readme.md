# UnicodeForUs—the open source repository of fun unicode characters

Frustrated by the disappearance of unicodeairplaneforyou.com, I decided to make a 
repository of fun unicode characters that belonged to everyone. With any luck, next time
you want to copy and paste a fun unicode character somewhere, you'll end up here!

## Contributing is super easy!

The *easiest* way to contribute is to file an issue on this repo, and I'll add your character
when I get around to it.

The *best* way to contribute is to send a pull request. This makes it much more likely 
I"ll add your character in a timely manner. Fork this repository, clone it
and run the script `char.py [your character] [text name]` (ex, `./char.py ✈ airplane`.)
This will generate the page 
in the proper format in the `characters` subdirectory. If you want to preview the site,
run `jekyll --auto --server` (`gem install jekyll` if you don't have it), and it will
create a server on localhost:4000 that you can use to preview your changes. Once you're 
happy, commit the result, push it to your fork, and send me a pull request.


There's a file called `build.sh` in the repo which I use when I'm deploying unicodefor.us.
Don't run `build.sh` unless you know what you're doing.

## “But dtb, what does fun mean?!?”

In the context of this repo, I am the dictator of fun. My current thinking is this: ✈ is 
fun, ☃ is fun, → is *not* fun (although quite handy, I admit.) The reason I want to be 
picky here is that there are already lots of resources that list every single unicode 
character. This distinguishes itself by being *not* that.

