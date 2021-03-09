function newMessage(topicName) {
  // Write your code here

  // Select p tag
  const targetTag = document.getElementByTag('p')

  // Remove style from all p tags
  document.getElementByTag('p').forEach(tag => {
    // remove style
    tag.style = ''
  })

  // If exist, add style.
  if (targetTag) {
    targetTag.style.backgroundColor = 'red'
  }
}

// Example case
document.body.innerHTML = `<div>
  <p data-topic-name="discussion">General discussion</p>
  <p data-topic-name="bugs">Bugs</p>
  <p data-topic-name="animals">Animals</p>
</div>`;
newMessage("discussion");
console.log(document.body.innerHTML);