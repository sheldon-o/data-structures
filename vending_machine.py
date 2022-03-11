class VendingMachine():
  def __init(self,num_items,item_price):
    self.num_items=num_items
    self.item_price=item_price
  def buy(self,req_items,money):
    if (req_items <= self.num_items):
      x = req_items*self.item_price
      if( money>=x):
        self.num_items=self.num_items-req_items
        return (money-x)
      else:
        return ("not enough coins")
    else:
      
      return ("not enough items in the machine")
