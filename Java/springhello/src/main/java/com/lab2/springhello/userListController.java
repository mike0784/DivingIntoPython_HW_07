package com.lab2.springhello;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.ModelAndView;
//import org.springframework.web.servlet.mvc.Controller;
import org.springframework.stereotype.Controller;
import com.lab2.springhello.UsersList;
@Controller
public class userListController 
//implements nController 
{

	public ModelAndView handleRequest(HttpServletRequest arg0,
			HttpServletResponse arg1) throws Exception {

		UsersList userList = new UsersList();
		
		ModelAndView modelAndView = new ModelAndView("userList");
		modelAndView.addObject("userList", UsersList.getUserList());

		return modelAndView;
	}
}
