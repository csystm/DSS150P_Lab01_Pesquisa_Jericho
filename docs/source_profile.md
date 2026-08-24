# Source Profile Interpretation

## customers.csv

**Shape:** 250 rows × 7 columns

### Observations

1. **Duplicate and key integrity risk**  
   - `customer_id` has only 247 distinct values out of 250 rows.  
   - There are 2 fully duplicated rows.  
   - This suggests the identifier may not be unique, which could break downstream joins and aggregations. A future pipeline must validate uniqueness or implement a deduplication policy.

2. **Missing values in contact/location fields**  
   - `email` has 3 missing values, `city` has 2 missing values.  
   - These fields are likely important for customer communication or segmentation. Missing data may need to be flagged, imputed, or treated as optional depending on business rules.

3. **Date column stored as string**  
   - `signup_date` is read as `object`/string, not as a date type.  
   - A pipeline must parse this column to a proper date/time type to support date-based analysis, sorting, or partitioning.

4. **Categorical field**  
   - `customer_segment` has 4 distinct values (e.g., Professional, Retail, SME, Student).  
   - This field can be used for segmentation but should be validated against a controlled vocabulary to prevent unexpected categories.


## orders.json

**Shape:** 250 rows × 9 columns

### Observations

1. **Nested JSON structure in `shipping`**  
   - The `shipping` column contains a nested object with `region` and `method`.  
   - This semi-structured data must be flattened (e.g., extracting `shipping.region` and `shipping.method` as separate columns) before loading into a relational table or for analysis.

2. **Timestamp stored as string**  
   - `order_timestamp` is read as a string, not as a timestamp.  
   - The values are in ISO-like format (`2026-06-27T03:27:00`). A pipeline should parse this to a proper timestamp type to enable time-series analysis and incremental loading.

3. **Unique identifier**  
   - `order_id` has 250 distinct values, one per record.  
   - This column appears to be a reliable primary key and can be used for deduplication and lookups.

4. **Numeric fields have sensible ranges**  
   - `item_count` ranges 1–8, `subtotal` 214.4–11997.73, `shipping_fee` 0–149, `total_amount` 214.4–12096.73.  
   - `shipping_fee` can be 0 (likely for `Pickup` method). The relationship `total_amount = subtotal + shipping_fee` holds in the sample.  
   - These ranges and relationships can be used in data quality checks (e.g., total_amount must be ≥ subtotal).


## products.parquet

**Shape:** 200 rows × 7 columns

### Observations

1. **Clean and complete data**  
   - No missing values, no fully duplicated rows.  
   - This file appears well-structured and ready for direct use, but it is still necessary to validate uniqueness of `product_id` (200 distinct values for 200 rows) and domain ranges.

2. **Unique identifier**  
   - `product_id` has exactly 200 distinct values, matching the row count.  
   - This column can serve as a primary key for the products table.

3. **Wide numeric ranges**  
   - `unit_price` ranges from 392.85 to 84,796.84.  
   - `stock_quantity` ranges 0–250, where 0 may indicate out-of-stock items.  
   - A pipeline should include checks for negative prices (none found) and stock levels (non-negative, 0 allowed).

4. **Categorical fields with limited distinct values**  
   - `category` and `brand` each have 6 distinct values.  
   - These are suitable for dictionary/controlled-vocabulary validation to prevent future schema drift.