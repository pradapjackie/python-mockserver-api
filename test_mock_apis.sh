#!/bin/bash

BASE_URL="http://127.0.0.1:5000"

declare -a endpoints=(
  "/api/user/1"
  "/api/user"
  "/api/user/1" # PUT
  "/api/user/1" # DELETE
  "/api/products"
  "/api/order/100"
  "/api/order"
  "/api/login"
  "/api/logout"
  "/api/health"
  "/api/notifications"
  "/api/settings"
  "/api/settings" # PUT
  "/api/profile"
  "/api/profile" # PATCH
  "/api/reports"
  "/api/upload"
)

declare -a methods=(
  "GET"
  "POST"
  "PUT"
  "DELETE"
  "GET"
  "GET"
  "POST"
  "POST"
  "POST"
  "GET"
  "GET"
  "GET"
  "PUT"
  "GET"
  "PATCH"
  "GET"
  "POST"
)

declare -a payloads=(
  ""
  '{"name": "New User"}'
  '{"name": "Updated"}'
  ""
  ""
  ""
  '{"item": "Book"}'
  '{"username": "admin"}'
  ""
  ""
  ""
  ""
  '{"theme": "light"}'
  ""
  '{"name": "Jane"}'
  ""
  ""
)

echo "Testing all mock API endpoints..."

for i in "${!endpoints[@]}"; do
  method=${methods[$i]}
  url="$BASE_URL${endpoints[$i]}"
  data=${payloads[$i]}
  echo
  echo "===== $method $url ====="
  if [[ "$method" == "GET" || "$method" == "DELETE" ]]; then
    curl -s -X $method "$url" -H "Content-Type: application/json"
  else
    curl -s -X $method "$url" -H "Content-Type: application/json" -d "$data"
  fi
  echo
done