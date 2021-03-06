-- upgrade --
CREATE TABLE IF NOT EXISTS "addresses" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255),
    "country" VARCHAR(100) NOT NULL,
    "region" VARCHAR(100) NOT NULL,
    "city" VARCHAR(100) NOT NULL,
    "street" VARCHAR(100) NOT NULL,
    "index" VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS "roles" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(25) NOT NULL UNIQUE,
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "lastname" VARCHAR(20) NOT NULL,
    "firstname" VARCHAR(50),
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "phone" VARCHAR(25),
    "password" VARCHAR(255),
    "avatar" VARCHAR(255),
    "email_confirmed_at" TIMESTAMP,
    "created_at" TIMESTAMP   DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP   DEFAULT CURRENT_TIMESTAMP,
    "is_actif" INT NOT NULL  DEFAULT 1
);
CREATE TABLE IF NOT EXISTS "notifications" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "type" VARCHAR(255) NOT NULL,
    "read_at" TIMESTAMP,
    "data" JSON,
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "user_id" BIGINT REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "verify_codes" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "code" VARCHAR(255) NOT NULL UNIQUE,
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "stores" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    "contact" VARCHAR(100),
    "address" VARCHAR(100),
    "website" VARCHAR(100),
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "owner_id" BIGINT REFERENCES "users" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "brands" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "categories" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "parent_id" BIGINT REFERENCES "categories" ("id") ON DELETE SET NULL
);
CREATE TABLE IF NOT EXISTS "products" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "slug" VARCHAR(255),
    "description" TEXT,
    "price" VARCHAR(40) NOT NULL  DEFAULT 0,
    "quantity" INT NOT NULL  DEFAULT 0,
    "barcode" VARCHAR(13),
    "vat" VARCHAR(40) NOT NULL  DEFAULT 0,
    "weight" VARCHAR(40) NOT NULL  DEFAULT 0,
    "length" VARCHAR(40) NOT NULL  DEFAULT 0,
    "height" VARCHAR(40) NOT NULL  DEFAULT 0,
    "width" VARCHAR(40) NOT NULL  DEFAULT 0,
    "brand_id" BIGINT REFERENCES "brands" ("id") ON DELETE SET NULL,
    "category_id" BIGINT REFERENCES "categories" ("id") ON DELETE SET NULL
);
CREATE TABLE IF NOT EXISTS "images" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "url" VARCHAR(255) NOT NULL,
    "is_main" INT NOT NULL  DEFAULT 0,
    "product_id" BIGINT REFERENCES "products" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSON NOT NULL
);
CREATE TABLE IF NOT EXISTS "user_roles" (
    "users_id" BIGINT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE,
    "role_id" BIGINT NOT NULL REFERENCES "roles" ("id") ON DELETE CASCADE
);
