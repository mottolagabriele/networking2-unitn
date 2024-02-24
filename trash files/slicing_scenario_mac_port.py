
                # Destination Mapping [router --> MAC Destination --> Eth Port Output]
        self.mac_to_port = {
            "sw0": {
                "00:00:00:00:01:01": 1,  # Porta su sw0 collegata a h0
                "00:00:00:02:02:01": 2,  # Porta su sw0 collegata a s0
                "00:00:00:01:00:01": 3,  # Porta su sw0 collegata a sw1
                "00:00:00:02:00:01": 4   # Porta su sw0 collegata a sw2
            },
            "sw1": {
                "00:00:00:01:01:01": 1,  # Porta su sw1 collegata a h1
                "00:00:00:01:01:02": 2,  # Porta su sw1 collegata a h2
                "00:00:00:01:01:03": 3,  # Porta su sw1 collegata a h3
                "00:00:00:01:02:01": 4   # Porta su sw1 collegata a sw3
            },
            "sw2": {
                "00:00:00:02:01:01": 1,  # Porta su sw2 collegata a h4
                "00:00:00:02:01:02": 2,  # Porta su sw2 collegata a h5
                "00:00:00:02:01:03": 3,  # Porta su sw2 collegata a h6
                "00:00:00:02:02:01": 4   # Porta su sw2 collegata a sw4
            },
            "sw3": {
                "00:00:00:01:02:01": 1,  # Porta su sw3 collegata a s1
                "00:00:00:01:02:02": 2   # Porta su sw3 collegata a s2
            },
            "sw4": {
                "00:00:00:02:02:01": 1,  # Porta su sw4 collegata a s3
                "00:00:00:02:02:02": 2   # Porta su sw4 collegata a s4
            },
            "sw5": {
                "00:00:00:02:00:01": 1,  # Porta su sw5 collegata a h4
                "00:00:00:02:00:02": 2,  # Porta su sw5 collegata a h5
                "00:00:00:02:00:03": 3   # Porta su sw5 collegata a h6
            },
            "sw6": {
                "00:00:00:02:02:01": 1,  # Porta su sw6 collegata a s3
                "00:00:00:02:02:02": 2   # Porta su sw6 collegata a s4
            }
        }