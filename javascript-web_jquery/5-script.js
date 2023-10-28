$(function() {
    $("#add_item").click(function() {
        let newItem = $("<li>Item</li>"); // item we should add
        
        $("ul.my_list").append(newItem); // we add the new item li
    });
});
