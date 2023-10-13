// we call the id add_item
const divAddItem =  document.querySelector("#add_item");

divAddItem.addEventListener('click', addItem);

// function that adds a new item when clicking on add item
function addItem() {
    var newItem = document.createElement('li');
    newItem.appendChild(document.createTextNode('Item'));

    var myList =  document.querySelector('.my_list');

    myList.appendChild(newItem);
}