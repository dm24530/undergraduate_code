package aaa;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.Map;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletRequestWrapper;

/**
 * Servlet Filter implementation class EncodingFilter
 */
@WebFilter(asyncSupported = true, urlPatterns = { "/*" })
public class EncodingFilter implements Filter {

	public void destroy() {
		// TODO Auto-generated method stub
	}


	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
		HttpServletRequest httpServletRequest=(HttpServletRequest) request;//处理请求乱码
		HttpServletRequest myRequest=new MyRequest(httpServletRequest);
		response.setContentType("text/html;charset=utf-8");	//处理响应乱码
		chain.doFilter(myRequest, response);
	}
	
	
	class MyRequest extends HttpServletRequestWrapper{
		private HttpServletRequest request;
		private boolean hasEncode;
		public MyRequest(HttpServletRequest request) {
			super(request);
			this.request=request;
		}
		//对需要增强的方法进行覆盖
		@Override
		public Map getParameterMap() {   //前端所提交请求中的请求参数和请求参数值的映射关系
			String method=request.getMethod();
			if(method.equalsIgnoreCase("post")) {//比较字符串 忽略大小写
				//post请求
				try {
					//处理post乱码
					request.setCharacterEncoding("utf-8");
					return request.getParameterMap();
				}catch(UnsupportedEncodingException e) {
					e.printStackTrace();
				}
			}else if(method.equalsIgnoreCase("get")) {
				//get请求
				Map<String,String[]> parameterMap=request.getParameterMap();
				if(!hasEncode) { //确保get手动编码逻辑只运行一次
					for(String parameterName:parameterMap.keySet()) {
						String[] values=parameterMap.get(parameterMap);
						if(values!=null) {
							for(int i=0;i<values.length;i++) {
								try {
									values[i]=new String(values[i].getBytes("ISO-8859-1"),"utf-8");
								}catch(UnsupportedEncodingException e) {
									e.printStackTrace();
								}
							}
						}
					}
					hasEncode=true;
				}
				return parameterMap;
			}
			return super.getParameterMap();
		}
		@Override
		public String getParameter(String name) {
			Map<String,String[]> parameterMap=getParameterMap();
			String[] values=parameterMap.get(name);
			if(values==null) {
				return null;
			}
			return values[0];
		}
		@Override
		public String[] getParameterValues(String name) {
			Map<String,String[]> parameterMap=getParameterMap();
			String[] values=parameterMap.get(name);
			return values;
		}
	}
	
	public void init(FilterConfig fConfig) throws ServletException {
		
	}
	
	
}
