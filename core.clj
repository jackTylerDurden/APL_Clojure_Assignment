(import '(javax.swing JFrame JLabel JTextField JButton JOptionPane)
        '(java.awt.event ActionListener)
        '(java.awt FlowLayout))

(let [frame (new JFrame "Clojure Assignment")
      first-name-label (new JLabel "First Name")
      first-name-text (new JTextField 20)      
      last-name-label (new JLabel "Last Name")
      last-name-text (new JTextField 20)      
      submit-button (new JButton "Submit")
      submit-label( new JLabel "")
      submit-message "Thank you for submitting the form"]      
      (. submit-button
        (addActionListener
           (proxy [ActionListener] []
                (actionPerformed [evt]                    
                  (JOptionPane/showMessageDialog frame submit-message)
                )
            )
        )
      )
    (doto frame 
                (.setDefaultCloseOperation (JFrame/EXIT_ON_CLOSE)) ;uncomment this line to quit app on frame close
                (.setLayout (new FlowLayout 3 25 25))
                (.add first-name-label)
                (.add first-name-text)
                (.add last-name-label)
                (.add last-name-text)
                (.add submit-button)
                (.add submit-label)
                (.setSize 400 300)
                (.setVisible true)))