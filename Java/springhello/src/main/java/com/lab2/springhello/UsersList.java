package com.lab2.springhello;
 
import java.util.LinkedList;
import java.util.List;
 
import com.lab2.springhello.User;
 
public class UsersList{
 
	private static List<User> userList;
 
	static {
		User user1 = new User();
		user1.setName("Vasya");
		User user2 = new User();
		user2.setName("Dima Pyrogof");
		User user3 = new User();
		user3.setName("Marusa");

		userList = new LinkedList<User>();
		userList.add(user1);
		userList.add(user2);
		userList.add(user3);
	}
 
	public static List<User> getUserList() {
		return userList;
	}	
}