title: Slide Title
subtitle: Subtitle
class: image

![Mobile vs desktop users](image.png)

---

title: 
class: big

---

title: title
subtitle: Subtitle
class: segue dark nobackground

---
  <slide>
    <hgroup>
      <h2>This slide was input as HTML</h2>
    </hgroup>
    <article>
      <ul>
        <li>Titles are formatted as Open Sans with bold applied and font size is set at 45</li>
        <li>Title capitalization is title case
          <ul>
            <li>Subtitle capitalization is title case</li>
          </ul>
        </li>
        <li>Subtitle capitalization is title case</li>
        <li>Titles and subtitles should never have a period at the end</li>
      </ul>
    </article>
  </slide>
---

title: Agenda
class: big
build_lists: true

Things we'll cover (list should build):

- Bullet1
- Bullet2
- Bullet3

---

title: Today
class: nobackground fill

![Many kinds of devices.](image.png)

<footer class="source">source: place source info here</footer>

---

title: Big Title Slide
class: title-slide

---

title: Code Example

Media Queries are sweet:

<pre class="prettyprint" data-lang="css">
@media screen and (max-width: 640px) {
  #sidebar { display: none; }
}
</pre>

---

title: Once more, with JavaScript

<pre class="prettyprint" data-lang="javascript">
function isSmall() {
  return window.matchMedia("(min-device-width: ???)").matches;
}

function hasTouch() {
  return Modernizr.touch;
}

function detectFormFactor() {
  var device = DESKTOP;
  if (hasTouch()) {
    device = isSmall() ? PHONE : TABLET;
  }
  return device;
}
</pre>

---

title: Centered content
content_class: flexbox vcenter

This content should be centered!
