Create and Activate Virtual Environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install Dependencies:

```bash
pip install -r requirements.txt
```
# Question 1 Get lowest local price
1. Get name, address, open times, menu items, & prices for Village from Yelp API
2. Get top-rated 5 restaurants in 2 km with similar menu items
3. DISPLAY menu items & prices for Village + each restaurant

## Output:-
![Screenshot 2024-12-16 011201](https://github.com/user-attachments/assets/eadbfbcb-46cf-4fa5-8d39-d6e6c1160fd7)

# Question 2 Get busy times & bad weather
4. Get Village busy times from GMaps API
5. Get temperature & rain near Village
6. DISPLAY both

## Output:-
![Screenshot 2024-12-16 011218](https://github.com/user-attachments/assets/a0a96598-5e7d-40b5-acc2-51075a4b8f84)

# Question 3 DISPLAY Village menu with predicted prices using ANY ML algo:
7.1 Temp is < 45 deg. Fahrenheit (note API returns Kelvin, convert to F)
7.2 It will snow or get moderate or heavy rain
7.3 Village is busier than usual
>THEN
Price should be more than lowest local price
>ELSE
Price should be lowest local price

## Output:-
![Screenshot 2024-12-16 011232](https://github.com/user-attachments/assets/d112a2a6-5687-4c13-84a4-fc9cbda11476)

