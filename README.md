# Ntwaalako Back end 
Ntwaalako is a ride sharing application that is aimed at connecting riders and drivers, The goal of this is to get to have a seemless mode of payment to avoid hustles in long distance travel and in payments 


The MVP objectives are :
 
- Login
- Register Vehicles
- Register Drivers 
- Request for a trip
- Pay for the Trip using lnd hold invoices
- Begin and End of trip 





## Developer Setup

Create a new python virtual env (>=3.9 preferably, but _may_ work with lower versions). Install the requirements into that environment with pip

```bash
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file from the `.env.example` file in the project root directory. Customise the values to fit your scenario. For purely local development, you  strictly need to update all the fields in that file:



## Running the application

Run any pending migrations and start the application

```bash
python manage makemigrations

python manage migrate

python manage runserver

```

## The next added features :

- Add ability for every user to create wallets  

 