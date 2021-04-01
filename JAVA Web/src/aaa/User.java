package aaa;

public class User {
	private String id;
	private String username; // 用户姓名
	private String password; // 用户密码
	private String name;
	private String sex;
	private String phone;
	private String birthday;
	private String hire_date;
	private String position;
	private String qualification;
	private String experience;
	private String flag;
	private String super_id;
	
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getSex() {
		return sex;
	}
	public void setSex(String sex) {
		this.sex = sex;
	}
	public String getPhone() {
		return phone;
	}
	public void setPhone(String phone) {
		this.phone = phone;
	}
	public String getBirthday() {
		return birthday;
	}
	public void setBirthday(String birthday) {
		this.birthday = birthday;
	}
	public String getHire_date() {
		return hire_date;
	}
	public void setHire_date(String hire_date) {
		this.hire_date = hire_date;
	}
	public String getPosition() {
		return position;
	}
	public void setPosition(String position) {
		this.position = position;
	}
	public String getQualification() {
		return qualification;
	}
	public void setQualification(String qualification) {
		this.qualification = qualification;
	}
	public String getExperience() {
		return experience;
	}
	public void setExperience(String experience) {
		this.experience = experience;
	}
	public String getFlag() {
		return flag;
	}
	public void setFlag(String flag) {
		this.flag = flag;
	}
	public String getSuper_id() {
		return super_id;
	}
	public void setSuper_id(String super_id) {
		this.super_id = super_id;
	}
	
	
	public String toString() {
		return "User{" +
				"id=" + id +
				", name='" + name + '\'' +
				", phone='" + phone + '\'' +
				", username='" + username + '\'' +
				", password='" + password + '\'' +
				", sex='"+sex+'\''+
				",birthday='"+birthday+'\''+
				",hire_date='"+hire_date+'\''+
				",position='"+position+'\''+
				",qualification='"+qualification+'\''+
				",experience='"+experience+'\''+
				",flag='"+flag+'\''+
				",super_id='"+super_id+'\''+
				'}';
	}
}
