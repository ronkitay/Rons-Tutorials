package hello;

/**
 * @author Ron Kitay
 * @since 25/11/15
 */
public class MyClass {

    private String someString;
    private int someInt;

    public MyClass() {
    }

    public MyClass(String someString, int someInt) {
        this.someString = someString;
        this.someInt = someInt;
    }

    public String getSomeString() {
        return someString;
    }

    public void setSomeString(String someString) {
        this.someString = someString;
    }

    public int getSomeInt() {
        return someInt;
    }

    public void setSomeInt(int someInt) {
        this.someInt = someInt;
    }

    public void set(String paramName, Object paramValue) {
        throw new IllegalArgumentException(paramName);
    }

    @Override
    public String toString() {
        return "MyClass{" +
                "someString='" + someString + '\'' +
                ", someInt=" + someInt +
                '}';
    }
}
