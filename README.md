# inventry-stock-control-system
# Inventory Management System – Testing Documentation

## 1. Testing Objectives
Verify product registration, stock management, sales processing, calculations, and inventory reports.

## 2. Product Registration Tests

| Test | Input | Expected Result |
|---|---|---|
| Add valid product | P001, Sugar | Product registered |
| Add duplicate ID | P001 | Registration rejected |
| Enter negative buying price | -100 | Rejected |
| Enter negative selling price | -150 | Rejected |
| Enter negative quantity | -5 | Rejected |
| Search existing product | P001 | Product displayed |
| Search unknown product | P999 | Product not found |

## 3. Stock Management Tests

| Test | Action | Expected Result |
|---|---|---|
| Update product quantity | Add 10 units | Stock updated |
| Remove available stock | Remove 2 units | Stock reduced |
| Remove more than available | Remove 100 units | Operation rejected |
| Check low stock | Quantity 4 | Low-stock warning |
| Check normal stock | Quantity 10 | No low-stock warning |

## 4. Sales Tests

| Test | Input | Expected Result |
|---|---|---|
| Valid sale | P001, quantity 2 | Sale completed |
| Sale above stock | Quantity greater than stock | Rejected |
| Sale of unknown product | P999 | Rejected |
| Zero quantity | 0 | Rejected |
| Negative quantity | -2 | Rejected |

## 5. Financial Calculation Tests
- Confirm profit per unit equals selling price minus buying price.
- Confirm total profit uses the quantity sold.
- Confirm stock value uses buying price multiplied by available quantity.
- Confirm sales reports display correct revenue and profit.

## 6. Data Storage Tests
Where JSON persistence is implemented:
- Save products and sales.
- Reload saved records.
- Confirm records remain available after restarting the application.
- Handle missing or invalid JSON files.

## 7. Conclusion
These tests verify the main inventory operations. Results should be confirmed by running the application; the listed outcomes are expected results, not automatically executed test results.
