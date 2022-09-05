// Time Conversion

const time_convert = (old_time) => {
    let time_element = old_time.split(':')
    let APM = time_element[2].slice(2)

    if (Number(time_element[0]) < 12 && APM === 'PM') {
        time_element[0] = 12 + Number(time_element[0])
    }
    if (Number(time_element[0]) === 12  && APM === 'AM') {
        time_element[0] = '00'
    }

    time_element[2] = time_element[2].slice(0, 2)
    time_string = String(time_element).replaceAll(',', ':')
    console.log(time_string)
    // return time_string
}

const nt = '12:00:00AM'
time_convert(nt)