## पायथन कोडसह व्हिडिओ रेकॉर्ड करा

आता एक व्हिडिओ रेकॉर्ड करा!

- `capture`() </code> काढून टाकण्यासाठी आपल्या कोडमध्ये सुधारणा करा आणि त्याऐवजी `start_recording()` आणि `stop_recording()` जोडा

आपला कोड आता यासारखा दिसला पाहिजे:
```python
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/video.h264')
    sleep(5)
    camera.stop_recording()
    camera.stop_preview()
```

- कोड चालवा.

आपल्या रास्पबेरी पाईने प्रिव्यू उघडावा, 5 सेकंदाचा व्हिडिओ रेकॉर्ड करावा आणि नंतर प्रिव्यू बंद करा.

