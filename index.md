---
layout: default
title: "Jona's Website"
fulltitle: "Personal website of Jona Koudijs. Read about me!"
excerpt: This is the greatest website on earth. Share! Like! Subscribe! I'm dead inside!
---

<!-- block: hero -->

<div class="section">

  <div class="container hero">
    <div class="row content-block hero-name header-text">
      <div class="column">Jona Koudijs</div>
    </div>
    <div class="row content-block hero-title header-text">
      <div class="column" id="hero-title">DevOps Engineer</div>
    </div>
  </div>

  <div class="container main-line hero-line"></div>

</div>

<!-- block: about -->

<div class="section" id="about">

  <div class="container main-line main-line-top"></div>

  <a class="anchor"></a>
  <div class="container">
    <div class="row">
      <div class="one-half column text">
        Hello! I'm Jona Koudijs an Infrastructure Engineer & Developer with over {{ "now" | date: "%Y" | minus: 2011 }} years of work experience.
        Like most I started tinkering away in my room with old servers and coding my first website. And I never stopped since.
        <br/><br/>
        In my spare time I like to listen and find (new) music, going to concerts and try to spend as much time as I can with my family and friends.
        Check out my latest music related activity <a href="#music">below</a>!

        <hr/>

        <h5>Website</h5>
        I have a few ideas on improvements for this website already but if you have any suggestions or found a bug, please let me know.
        The full source code is available on <a href="https://github.com/jonakoudijs/jonakoudijs.github.io">Github</a>.

        <hr/>

        <h5>Contact</h5>
        You can find/contact me on various places like:
        <div class="music-object">
            <svg class="icon"><use xlink:href="#icon-linkedin" /></svg>
          <a href="https://www.linkedin.com/in/jonakoudijs">LinkedIn</a>
        </div>
        <div class="music-object">
          <svg class="icon"><use xlink:href="#icon-github" /></svg>
          <a href="https://github.com/jonakoudijs">Github</a>
        </div>
        <div class="music-object">
          <svg class="icon"><use xlink:href="#icon-gitlab" /></svg>
          <a href="https://gitlab.com/jonakoudijs">Gitlab</a>
        </div>
        <div class="music-object">
          <svg class="icon"><use xlink:href="#icon-package" /></svg>
          <a href="https://stackshare.io/jona">StackShare</a>
        </div>
        <div class="music-object">
          <svg class="icon"><use xlink:href="#icon-twitter" /></svg>
          <a href="https://twitter.com/jonakoudijs">Twitter</a>
        </div>

      </div>
      <div class="one-half column about-img">
        <img src="{{ site.photo }}" class="about-img" />
      </div>
    </div>
  </div>

  <div class="container main-line main-line-bottom"></div>

</div>

<!-- block: music -->

<div class="section" id="music">

  <div class="container main-line main-line-top"></div>

  <div class="container">
    <div class="row">
      <div class="one-half column text">
        In my spare time I like to listen to all different kinds of music and go to concerts and festivals.
        My taste is mostly relaxed (indie) but it really differs based on my mood.
        <br/><br/>
        If you have any recommendations, please let me know! Below you can see my top artists on
        <a href="https://www.spotify.com">Spotify</a>, my past concerts (powered by <a href="https://www.songkick.com/home">Songkick</a>)
        and what I am currently listening (if I am listening anything at the moment).

        <hr/>

        <h5>Top Artists</h5>
        <div id="music-top-artists"></div>

      </div>

      <div class="one-half column text">

        <h5>Past Concerts</h5>
        <div id="music-past-concerts"></div>

      </div>
    </div>

    <div class="row">
      <div class="column text">
        <hr/>
        <h5>Currently Playing</h5>
        <span class="u-pull-left">
          <svg class="icon icon-play"><use id="play-icon-use" xlink:href="#icon-pause-circle" /></svg>
        </span>
        <span id="nowplaying" class="u-pull-left"></span>
      </div>
    </div>
  </div>

</div>
