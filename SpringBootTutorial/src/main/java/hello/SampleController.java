package hello;

import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.stereotype.*;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import java.util.Arrays;
import java.util.Enumeration;

@Controller
@EnableAutoConfiguration
public class SampleController {

    @RequestMapping("/")
    @ResponseBody
    String home(HttpServletRequest request) {

        final Enumeration<String> headerNames = request.getHeaderNames();

        System.out.println("============================================================");
        System.out.println("Headers:");
        while (headerNames.hasMoreElements()) {
            final String headerName = headerNames.nextElement();
            final Enumeration<String> headers = request.getHeaders(headerName);

            while (headers.hasMoreElements()) {
                System.out.printf("Header <%s> - Value <%s>\n", headerName, headers.nextElement());
            }
        }
        System.out.println("============================================================\n");

        System.out.println("============================================================");
        System.out.println("Parameters:");
        final Enumeration<String> parameterNames = request.getParameterNames();
        while (parameterNames.hasMoreElements()) {
            final String parameterName = parameterNames.nextElement();
            final String[] parameterValues = request.getParameterValues(parameterName);
            System.out.printf("Parameter <%s> - Values <%s>\n", parameterName, Arrays.toString(parameterValues));
        }
        System.out.println("============================================================\n");

        return "Hello World!";
    }

    public static void main(String[] args) throws Exception {
        SpringApplication.run(SampleController.class, args);
    }
}