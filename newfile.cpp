



while(1){
cout << "Enter option:" << endl ;
cin >> selected_options;

switch(selected_options){
  {
    case "add":
      break;
    case "remove":
      break;
    case "change":
      break;
    case "description":
      getDescription();
      break;
    case "options":
      printf("Options List");
    case "quit":
      //quit program
      return(1);
    default:
      break;
  }
}
}


for(int i = 0; i< itemsInCart.size(); i++){
  if(itemsInCart[i] == item)
  {
    return "Item is already in cart";
  }
}
itemsInCart.push_back(item);
return "\n";
