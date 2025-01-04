def time_string(hours, minutes, time_format):
    if time_format == '24': 
        
        if hours < 10 and minutes >= 10:
            return f'0{hours}:{minutes}'
        if hours >= 10 and minutes < 10:
            return f'{hours}:0{minutes}'
        if hours < 10 and minutes <10: 
            return f'0{hours}:0{minutes}'   
        if hours >=10 and minutes >=10: 
            return f'{hours}:{minutes}'
        
    if time_format == '12':
        
        if hours <= 12:
            if hours == 0:
                return f"12:{minutes}am"
            if hours < 10 and minutes >= 10:
                return f'0{hours}:{minutes}am'
            if hours >= 10 and minutes < 10:
                return f'{hours}:0{minutes}am'
            if hours < 10 and minutes <10: 
                return f'0{hours}:0{minutes}am'   
            if hours >=10 and minutes >=10: 
                return f'{hours}:{minutes}am'
        
        if hours > 12:
            hours -= 12  
            if hours < 10 and minutes >= 10:
                return f'0{hours}:{minutes}pm'
            if hours >=10 and minutes < 10:
                return f'{hours}:0{minutes}pm'
            if hours < 10 and minutes <10: 
                return f'0{hours}:0{minutes}pm'   
            if hours >=10 and minutes >=10: 
                return f'{hours}:{minutes}pm'
            
    
if __name__ == "__main__":
    print(time_string(15, 38, '24'))
    print(time_string(8, 3, '24'))
    print(time_string(0, 5,'24'))
    print(time_string(11, 15, '12'))
    print(time_string(0, 7, '12'))
    print(time_string(7, 30, '12'))
    print(time_string(12, 46, '12'))
    print(time_string(13, 10, '12'))
    print(time_string(19, 2, '12'))
