#store Managing Console Application

### Run the code

`python store.py`

## Sample input

```
INVENTORY=>1|GoodDay250g|20|10
INVENTORY=>2|GoodDay500g|10|20

NEW-OFFER=>BuyXMore|1|1,2|2|10
SALE=>1|8;2|2
SALE=>1|8;2|1

STOCK=>1
STOCK=>2
SALE=>1|2;2|1

STOCK=>1
STOCK=>2

NEW-OFFER=>BuyXMore|1|1|2|10
SALE=>1|4;2|1
STOCK=>1
STOCK=>2

NEW-OFFER=>BuyXMore|2|1|4|20
SALE=>1|4;2|1
STOCK=>1
STOCK=>2

EXIT
```

## Sample Output

```
INVENTORY=>1|GoodDay250g|20|10
Inventory updated.
INVENTORY=>2|GoodDay500g|10|20
Inventory updated.

NEW-OFFER=>BuyXMore|1|1,2|2|10
Offer Added.
SALE=>1|8;2|2
== Bill ==
1 - GoodDay250g - 8 - 10 - 1 - 72
2 - GoodDay500g - 2 - 20 - 1 - 36
== Total ==
108
========
SALE=>1|8;2|1
== Bill ==
1 - GoodDay250g - 8 - 10 - N/A - 80
2 - GoodDay500g - 1 - 20 - N/A - 20
== Total ==
100
========

STOCK=>1
GoodDay250g - 20
STOCK=>2
GoodDay500g - 10
SALE=>1|2;2|1
== Bill ==
1 - GoodDay250g - 2 - 10 - N/A - 20
2 - GoodDay500g - 1 - 20 - N/A - 20
== Total ==
40
========

STOCK=>1
GoodDay250g - 20
STOCK=>2
GoodDay500g - 10

NEW-OFFER=>BuyXMore|1|1|2|10
Offer Added.
SALE=>1|4;2|1
== Bill ==
1 - GoodDay250g - 4 - 10 - 1 - 36
2 - GoodDay500g - 1 - 20 - N/A - 20
== Total ==
56
========
STOCK=>1
GoodDay250g - 20
STOCK=>2
GoodDay500g - 10

NEW-OFFER=>BuyXMore|2|1|4|20
Offer Added.
SALE=>1|4;2|1
== Bill ==
1 - GoodDay250g - 4 - 10 - 2 - 32
2 - GoodDay500g - 1 - 20 - N/A - 20
== Total ==
52
========
STOCK=>1
GoodDay250g - 20
STOCK=>2
GoodDay500g - 10

EXIT
Sign Off...
```
