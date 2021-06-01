//
//  ViewController.swift
//  Helloworrd
//
//  Created by Jang Dayoung on 11/1/20.
//  Copyright © 2020 Jang Dayoung. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet var lblHello: UILabel!
    
    @IBOutlet var txtName: UITextField!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func btbSend(_ sender: UIButton) {
        lblHello.text = "Hello, " + txtName.text!
    }
    
}

