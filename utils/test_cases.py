

# for maintainability, we can seperate web test cases by page name but I just listed every case in same array

def test_cases(number):
    return testCases[number]

testCases = [
    # [severity, description]
    ['Blocker', 'WHEN user goes to main page, THEN page should be loaded'],
    ['Blocker', 'In Main page, WHEN user click "Sign in" button, THEN User should see Sign in Page'],
    ['Blocker', 'In Login Page, WHEN user login with a valid user, THEN User should see Home Page'],
    ['Blocker', 'In Login Page, WHEN user login with a invalid user, THEN User should see Error Message'],
    ['Blocker', 'In Login page, WHEN user click "Sign up" button, THEN User should see Sign up Page'],
    ['Blocker', 'In Login page, WHEN user click "Need help?" , THEN User should see Password reset screen'],
    ['Medium', 'In Login page, WHEN user click "Remember me" , THEN User should see remember me checkbox checked'],
    ['Medium', 'In Login page, WHEN user click "Login with organisation me" , THEN User should get organisation login page'],
]