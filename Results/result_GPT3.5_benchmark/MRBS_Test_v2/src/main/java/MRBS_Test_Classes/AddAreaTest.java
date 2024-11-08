package MRBS_Test_Classes;
//import config.DriverConfig;
import org.testng.annotations.*;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
//import testcases.mrbs.model_based_dataset.sql.Area;
import MRBS_Test_Classes.sql.Constants;

public class AddAreaTest {
	private static WebDriver driver;

	@BeforeMethod
	public void setUp() throws Exception {

		System.setProperty("webdriver.chrome.driver",
				"D:\\anaconda3\\chromedriver.exe");
		driver = new ChromeDriver();
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		driver.get(Constants.BASE_URL);

		// Login User Administrator
		Thread.sleep(2000);
		driver.findElement(By.xpath("//input[@value=' Log in ']")).click();
		Thread.sleep(2000);
		driver.findElement(By.name("NewUserName")).clear();
		driver.findElement(By.name("NewUserName")).sendKeys(Constants.ADMIN_USER_NAME);
		driver.findElement(By.name("NewUserPassword")).clear();
		driver.findElement(By.name("NewUserPassword")).sendKeys(Constants.ADMIN_PASSWORD);
		driver.findElement(By.xpath("//div[@id='logon_submit']/input")).click();
		Thread.sleep(2000);
		driver.findElement(By.xpath("//a[text()='Rooms']")).click();
		Thread.sleep(2000);
		//TODO: Area.deleteArea("Area New");
	}

	@Test(priority = 0)
	public static void addAreaTest() throws Exception {

		driver.findElement(By.name("name")).clear();
		driver.findElement(By.name("name")).sendKeys("Area New");
		Thread.sleep(1000);

		driver.findElement(By.xpath("//input[@value='Add Area']")).click();
		Thread.sleep(2000);
		//try {
		Assert.assertEquals(driver.findElement(By.xpath("//option[text()='Area New']")).getText(), "Area New");
//		} catch (Exception e) {
//			e.printStackTrace();
//		}
	}

	@AfterMethod
	public void close() {
		driver.quit();
	}

	public static void jsClick(WebElement element) {
		((JavascriptExecutor) driver).executeScript("arguments[0].click();", element);
	}

	public boolean isElementPresent(By by) {
		try {
			driver.findElement(by);
			return true;
		} catch (org.openqa.selenium.NoSuchElementException e) {
			return false;
		}
	}

}
