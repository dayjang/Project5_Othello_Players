//
//  ViewController.swift
//  DatePicker
//
//  Created by Jang Dayoung on 11/3/20.
//  Copyright © 2020 Jang Dayoung. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    let timeSelector: Selector = #selector(ViewController.updateTime)
    let interval = 0
    var count = 0 
    
    @IBOutlet var lblCurrentTIme: UILabel!
    @IBOutlet var lblPickerTime: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func changeDatePicker(_ sender: UIDatePicker) {
        let datePickerView = sender
        let formatter = DateFormatter()
        formatter.dateFormat = "yyyy-mm-dd HH:mm EEE"
        
        lblPickerTime.text = "Seleced Datetime: " + formatter.string(from: datePickerView.date)
        
    }
    
}

