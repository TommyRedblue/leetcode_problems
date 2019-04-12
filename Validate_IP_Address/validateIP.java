class Solution {    
    
    public boolean isIPV4 (String IP) {
        String[] parts = IP.split("\\.");

        if(parts.length < 4 || parts.length > 4) return false; 
        
        if(IP.charAt(IP.length() - 1) == '.') return false; 

        
        for(int i = 0; i < parts.length; i++) {
            if(parts[i].length() < 1) return false; 

            if(parts[i].contains("-")) return false; 
            
            if(parts[i].charAt(0) == '0' && parts[i].length() != 1) return false;

            try{
                int num = Integer.parseInt(parts[i]);
                if (num > 255 || num < 0) {
                    return false;
                }
            } catch(Exception e){
                return false;
            }
        }
        
        return true;
    }
    
    
    public boolean isIPV6 (String IP) {
        
        String[] ipv6Chars = new String[]{"a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"};
        
        List<String> charList = Arrays.asList(ipv6Chars);
        
        String[] parts = IP.split(":");
         
        if(IP.charAt(IP.length() - 1) == ':') {
            return false;
        }
        
        if(parts.length != 8) return false;
        
        for(int i = 0; i < parts.length; i++) {
            String section = parts[i];
            
            if(section.length() < 1) return false;
            
            if(section.length() > 4) return false;
            
            for(int j = 0; j < section.length(); j++) {
                if(!charList.contains(Character.toString(section.charAt(j)))) {
                    return false;
                }
            }
        }
        return true;
    }
    
    
    public String validIPAddress(String IP) {
        if(IP.length() < 7) {
            return "Neither";
        } else if(isIPV4(IP)) {
            return "IPv4";
        } else if (isIPV6(IP)) {
            return "IPv6";
        } else {
            return "Neither";
        }
    }
}
