-- Basic Schema for orders.json

-- Create the lab schema if it does not exist
CREATE SCHEMA IF NOT EXISTS lab;

-- Create the orders table in the lab schema
CREATE TABLE IF NOT EXISTS lab.orders (
    order_id         TEXT PRIMARY KEY,               -- e.g., 'O00001'
    customer_id      TEXT NOT NULL,                  -- e.g., 'C0230'
    order_timestamp  TIMESTAMP NOT NULL,             -- parsed from ISO-like string
    status           TEXT NOT NULL,
    item_count       INTEGER NOT NULL,
    subtotal         NUMERIC(10,2) NOT NULL,
    shipping_fee     NUMERIC(10,2) NOT NULL,
    total_amount     NUMERIC(10,2) NOT NULL,
    shipping_region  TEXT NOT NULL,                  -- extracted from shipping.region
    shipping_method  TEXT NOT NULL,                  -- extracted from shipping.method
    CONSTRAINT ck_orders_item_count_positive CHECK (item_count > 0),
    CONSTRAINT ck_orders_total_amount_non_negative CHECK (total_amount >= 0),
    CONSTRAINT ck_orders_shipping_fee_non_negative CHECK (shipping_fee >= 0),
    CONSTRAINT ck_orders_status_allowed CHECK (status IN ('Packed','Delivered','Cancelled','Pending','Shipped','Paid'))
);

-- Index on customer_id for potential lookups
CREATE INDEX IF NOT EXISTS idx_orders_customer_id ON lab.orders(customer_id);