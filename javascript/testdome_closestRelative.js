function closestRelative(parent, relativeName) {
  const queue = [...parent.children];
  const tagName = relativeName.toUpperCase();

  let el;
  while (queue.length > 0) {
    el = queue.shift();
    if (el.tagName === tagName) return el;
    if (!el.hasChildNodes()) { continue; }

    for (const childEl of el.children) {
      queue.push(childEl);
    }
  }

  return null;
}

// Example case
document.body.innerHTML =
'<James>' +
  '<Dave></Dave>' +
  '<Mike></Mike>' +
  '<Sarah></Sarah>' +
'</James>';

let parent = document.getElementsByTagName('James')[0];
let relative = closestRelative(parent, 'Mike');
console.log(relative && relative.tagName); // prints MIKE