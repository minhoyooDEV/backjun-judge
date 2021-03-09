function showCustomers(customers, targetList) {
  customers.forEach(({ name, email }) => {
    (function(){
      const li = document.createElement('li');
      const nameEl = document.createElement('p');
      nameEl.innerText = name;
      li.appendChild(nameEl);

      nameEl.addEventListener('click', () => {
        if (li.children.length === 1) {
          const emailEl = document.createElement('p');
          emailEl.innerHTML = email;
          li.appendChild(emailEl);
        } else {
          li.removeChild(li.getElementsByTagName('p')[1])
        }
      })

      targetList.appendChild(li)
    })()
  });
}

document.body.innerHTML = `
<div>
  <ul id="customers">
  </ul>
</div>
`;
let customers = [
  { name: 'John', email: 'john@example.com' },
  { name: 'Mary', email: 'mary@example.com' },
];
showCustomers(customers, document.getElementById('customers'));

let customerParagraph = document.querySelectorAll('li > p')[0];
if (customerParagraph) {
  customerParagraph.click();
}
console.log(document.body.innerHTML);
