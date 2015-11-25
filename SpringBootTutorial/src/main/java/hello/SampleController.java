package hello;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import org.springframework.beans.BeansException;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.EnableAspectJAutoProxy;
import org.springframework.http.converter.HttpMessageNotWritableException;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.WebDataBinder;
import org.springframework.web.bind.annotation.*;

import javax.servlet.ServletInputStream;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.beans.PropertyEditorSupport;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.text.MessageFormat;
import java.util.Arrays;
import java.util.Enumeration;
import java.util.zip.GZIPOutputStream;

@Controller
@EnableAutoConfiguration
@EnableAspectJAutoProxy
@ComponentScan(basePackages = {"hello"})
public class SampleController implements ApplicationContextAware {

    @InitBinder
    public void initBinder(WebDataBinder binder) {
        binder.registerCustomEditor(MyParameters.class, new MyParametersEditor());
    }

    @RequestMapping("/test/**")
    @ResponseBody
    String test(HttpServletRequest request){
        return "You requested <" + request.getRequestURI().toString() + "?" + request.getQueryString() + ">" ;
    }

    @RequestMapping(value = "/")
//    @Response
    void home(
            HttpServletRequest request,
            HttpServletResponse response,
            @RequestParam(value = "zip", required = false, defaultValue = "true") boolean useZip,
            @RequestParam(value = "myjson", required = false) MyParameters myParameters,
            @RequestParam(value = "category", required = false) String[] headerWithMultipleValues,
            @RequestHeader(value = "id", required = false) String headerWithSingleValue) throws IOException {

//        response.setHeader("disposition-type", "attachment");
//        response.setHeader("disposition-param", "filename-param");
//        response.setHeader("filename-param", "filename");
//        response.setHeader("Content-Disposition","attachment; filename=\"xxx\"");
        response.setContentType("application/txt");
        if (useZip) response.setHeader("Content-Encoding", "gzip");
        OutputStream outputStream = response.getOutputStream();
        if (useZip) outputStream = new GZIPOutputStream(outputStream);

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(outputStream));

        for (int i = 0; i < 100000; i++) {
            bw.write("Hello zip world!\n");
        }
        bw.flush();
        bw.close();

//        try {Thread.sleep(5000);} catch (InterruptedException e) {}
//
//        for (int i = 0; i < 100000; i++) {
//            response.getOutputStream().println(i);
////            response.flushBuffer();
//
//            if (i > 10000) {
//                throw new HttpMessageNotWritableException("");
//            }
//
//            if (i%1000==0) {
//                response.getOutputStream().println("slepping ....");
////                response.flushBuffer();
//                try {Thread.sleep(1000);} catch (InterruptedException e) {}
//            }
//        }

//        final Enumeration<String> headerNames = request.getHeaderNames();
//
//        final ServletOutputStream outputStream = response.getOutputStream();
//
//        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(outputStream));
//
//        StringBuilder sb= new StringBuilder();
//
//        bw.append("============================================================\n");
//        response.flushBuffer();
//        bw.append("Headers:\n");
//        response.flushBuffer();
//        while (headerNames.hasMoreElements()) {
//            final String headerName = headerNames.nextElement();
//            final Enumeration<String> headers = request.getHeaders(headerName);
//
//            while (headers.hasMoreElements()) {
//                bw.append(MessageFormat.format("Header <{0}> - Value <{1}>\n", headerName, headers.nextElement()));
//                response.flushBuffer();
//            }
//        }
//        bw.append("============================================================\n\n");
//        response.flushBuffer();
//

//        if (true) {
//            response.setStatus(500);
//            try {Thread.sleep(1000);} catch (InterruptedException e) {}
//            bw.flush();
//            try {Thread.sleep(1000);} catch (InterruptedException e) {}
//            bw.close();
//            try {Thread.sleep(1000);} catch (InterruptedException e) {}
//            throw new RuntimeException("");
//        }
//        bw.append("============================================================\n");
//        bw.append("Parameters:\n");
//        final Enumeration<String> parameterNames = request.getParameterNames();
//        while (parameterNames.hasMoreElements()) {
//            final String parameterName = parameterNames.nextElement();
//            final String[] parameterValues = request.getParameterValues(parameterName);
//            bw.append(MessageFormat.format("Parameter <{0}> - Values <{1}>\n", parameterName, Arrays.toString(parameterValues)));
//        }
//        bw.append("============================================================\n");
//
//        bw.append("My Parameters = " + myParameters + "\n\n");
//        bw.flush();

//        return bw.toString();
    }

    public static void main(String[] args) throws Exception {
        SpringApplication.run(SampleController.class, args);
    }

    @Override
    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {

    }

    //    @JsonDeserialize
    public static class MyParameters {

//        @JsonProperty
        private int abc;

        public void setAbc(int abc) {
            this.abc = abc;
        }

        public int getAbc() {
            return abc;
        }

        @Override
        public String toString() {
            return "MyParameters{" +
                    "abc=" + abc +
                    '}';
        }
    }

    private class MyParametersEditor extends PropertyEditorSupport {

        @Override
        public void setAsText(String text) throws IllegalArgumentException {
            ObjectMapper mapper = new ObjectMapper();

            MyParameters value = null;

            try {
//                value = new MyParameters();
                value = mapper.readValue(text, MyParameters.class);
//                JsonNode root = mapper.readTree(text);
//                value.setAbc(root.path("abc").asInt());
            } catch (IOException e) {
                e.printStackTrace();
            }

            setValue(value);
        }

    }
}