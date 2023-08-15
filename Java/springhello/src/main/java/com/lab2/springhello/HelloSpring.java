package com.lab2.springhello;
//import org.springframework.context.annotation.Bean;
//import org.springframework.context.annotation.Configuration;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;
//import com.lab2.springhello.UsersList;
//import org.springframework.web.servlet.ViewResolver;
//import org.springframework.web.servlet.view.InternalResourceViewResolver;


@Controller
public class HelloSpring {
 
	 @RequestMapping(value = "/")
	    public ModelAndView home() {
	        System.out.println("HomeController: Passing through...");
	        ModelAndView modelAndView = new ModelAndView("WEB-INF/views/home.jsp");
	    modelAndView.addObject("userList", UsersList.getUserList());
	 return modelAndView;
	}
}

/**
 * @Controller
public class HelloSpring {
 
    @RequestMapping(value = "/")
    public String home() {
        System.out.println("HomeController: Passing through...");
        return "WEB-INF/views/home.jsp";
    }
}
 * 
 * 
 * 
  @RequestMapping(value = "/")
    public ModelAndView home() {
        System.out.println("HomeController: Passing through...");
        ModelAndView modelAndView = new ModelAndView("WEB-INF/views/home.jsp");
    modelAndView.addObject("userList", UsersList.getUserList());

        return modelAndView;
    }

 * 
 * @Configuration
public class HelloSpring {
 
    // Resolve logical view names to .jsp resources in the /WEB-INF/views directory
    @Bean
    ViewResolver viewResolver() {
        InternalResourceViewResolver resolver = new InternalResourceViewResolver();
        resolver.setPrefix("WEB-INF/views/");
        resolver.setSuffix(".jsp");
        return resolver;
    }
}
 * 
 * 
 * @Controller
public class HelloSpring {
    @RequestMapping("/user")
       	 public ModelAndView list_users() {
 	       getUserList(@RequestParam ("name")String userName;
 	        return "list_users.html";
 	    } 
}
 * @author user
 *@Controller
	public class HelloSpring {

	    @RequestMapping("/helloWorld")
	    public ModelAndView helloWorld() {
	        ModelAndView mav = new ModelAndView();
	        mav.setViewName("helloWorld");
	        mav.addObject("message", "Hello World!");
	        return mav;
	    }
}
 */



