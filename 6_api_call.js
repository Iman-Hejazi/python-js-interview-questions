/*
You can use python for this task if you prefer.
in javascript:
1) using fetch function, write code to fetch data from "https://fakestoreapiserver.reactbd.com/users"
2) and print the values for each user to terminal
*/

async function getData(url) {

    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }

      const users = await response.json();
      for (const user of users) {
        console.log(user['name'])
    }
    } catch (error) {
      console.error(error.message);
    }
  }

const url = "https://fakestoreapiserver.reactbd.com/users";
getData(url)