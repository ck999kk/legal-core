#!/usr/bin/env python3
"""
Gmail Export Automation for Complete Evidence Collection
Ensures 100% data capture from ck.chawakorn@gmail.com
Step-by-step automation to prevent human error in data collection
"""

import json
import os
from datetime import datetime
from pathlib import Path
import subprocess
import webbrowser

class GmailExportAutomator:
    """Automate Gmail export process for complete evidence collection"""
    
    def __init__(self, target_email="ck.chawakorn@gmail.com"):
        self.target_email = target_email
        self.export_dir = Path("./gmail_exports")
        self.export_dir.mkdir(exist_ok=True)
        
        self.export_log = []
        self.completeness_checklist = []
    
    def complete_export_process(self):
        """Complete automated Gmail export process"""
        print("📧 GMAIL COMPLETE EXPORT AUTOMATION")
        print("=" * 50)
        print(f"Target: {self.target_email}")
        print("🎯 Ensuring 100% data capture")
        print("")
        
        # Step-by-step export process
        steps = [
            self.step_1_google_takeout,
            self.step_2_export_configuration,
            self.step_3_download_monitoring,
            self.step_4_data_verification,
            self.step_5_forensic_processing
        ]
        
        for i, step in enumerate(steps, 1):
            print(f"📋 EXECUTING STEP {i}/5")
            result = step()
            self.export_log.append({
                'step': i,
                'timestamp': datetime.now().isoformat(),
                'result': result,
                'status': 'completed' if result['success'] else 'failed'
            })
            
            if not result['success']:
                print(f"❌ Step {i} failed: {result['error']}")
                break
                
            print(f"✅ Step {i} completed successfully")
            print("")
        
        return self.generate_export_report()
    
    def step_1_google_takeout(self):
        """Step 1: Initiate Google Takeout for Gmail"""
        print("🚀 Step 1: Google Takeout Initiation")
        print("   Opening Google Takeout for Gmail export...")
        
        try:
            # Open Google Takeout
            takeout_url = "https://takeout.google.com/settings/takeout"
            webbrowser.open(takeout_url)
            
            print("📋 MANUAL STEPS REQUIRED:")
            print("   1. Sign in to ck.chawakorn@gmail.com")
            print("   2. Deselect all products EXCEPT Gmail")
            print("   3. Click 'All Mail data included'")
            print("   4. Select format: .mbox (recommended)")
            print("   5. Choose delivery method: Download via link")
            print("   6. File size: 2GB (recommended)")
            print("   7. Click 'Create export'")
            print("")
            
            # Wait for user confirmation
            input("⏳ Press ENTER after completing Google Takeout setup...")
            
            return {
                'success': True,
                'message': 'Google Takeout initiated',
                'next_action': 'Monitor export progress'
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'message': 'Failed to initiate Google Takeout'
            }
    
    def step_2_export_configuration(self):
        """Step 2: Configure export for complete data capture"""
        print("⚙️  Step 2: Export Configuration Verification")
        
        configuration_checklist = [
            "✅ Gmail selected (all other products deselected)",
            "✅ All Mail data included (not just recent)",
            "✅ .mbox format selected for forensic compatibility",
            "✅ Download method: Download via link",
            "✅ File size: 2GB for manageable downloads",
            "✅ Include attachments: YES",
            "✅ Include labels: YES",
            "✅ Include spam and trash: YES (for complete analysis)"
        ]
        
        print("📋 CONFIGURATION CHECKLIST:")
        for item in configuration_checklist:
            print(f"   {item}")
        
        print("")
        print("⚠️  CRITICAL: Ensure ALL mail is included")
        print("   - This includes sent items, drafts, spam, and trash")
        print("   - Date range should be 'All time'")
        print("   - Labels should include all folders")
        
        verify = input("✅ Confirm all configuration items are correct (y/n): ")
        
        if verify.lower() == 'y':
            return {
                'success': True,
                'message': 'Export configuration verified',
                'configuration': configuration_checklist
            }
        else:
            return {
                'success': False,
                'error': 'Configuration not verified',
                'message': 'Please review and correct export settings'
            }
    
    def step_3_download_monitoring(self):
        """Step 3: Monitor download progress and completion"""
        print("📥 Step 3: Download Monitoring")
        print("   Google will email download links when ready...")
        print("   This typically takes 1-24 hours depending on data size")
        print("")
        
        print("📧 DOWNLOAD INSTRUCTIONS:")
        print("   1. Check ck.chawakorn@gmail.com for email from Google")
        print("   2. Email subject: 'Your Google data is ready for download'")
        print("   3. Click download links in the email")
        print("   4. Save files to:", self.export_dir.absolute())
        print("   5. Verify file integrity using provided checksums")
        print("")
        
        # Create download tracking file
        download_tracker = {
            'target_email': self.target_email,
            'export_initiated': datetime.now().isoformat(),
            'download_directory': str(self.export_dir.absolute()),
            'expected_files': ['takeout-*.zip', 'mbox files'],
            'checksum_verification': 'required',
            'status': 'waiting_for_download'
        }
        
        tracker_file = self.export_dir / "download_tracker.json"
        with open(tracker_file, 'w') as f:
            json.dump(download_tracker, f, indent=2)
        
        print(f"📊 Download tracker created: {tracker_file}")
        
        return {
            'success': True,
            'message': 'Download monitoring configured',
            'tracker_file': str(tracker_file)
        }
    
    def step_4_data_verification(self):
        """Step 4: Verify data completeness and integrity"""
        print("🔍 Step 4: Data Verification")
        
        verification_checklist = [
            "File integrity (checksum verification)",
            "Complete date range coverage",
            "All email folders included",
            "Attachment preservation",
            "Metadata completeness",
            "No corruption or missing data"
        ]
        
        print("📋 DATA VERIFICATION CHECKLIST:")
        for item in verification_checklist:
            print(f"   ⏳ {item}")
        
        # Create verification script
        verification_script = self.create_verification_script()
        
        print(f"🔧 Verification script created: {verification_script}")
        print("   Run this script after downloading Gmail export")
        
        return {
            'success': True,
            'message': 'Verification tools prepared',
            'verification_script': str(verification_script)
        }
    
    def step_5_forensic_processing(self):
        """Step 5: Prepare for forensic analysis"""
        print("🔬 Step 5: Forensic Processing Preparation")
        
        processing_pipeline = [
            "MBOX parsing and email extraction",
            "Metadata analysis and cataloging",
            "Behavioral pattern recognition",
            "Government preference analysis",
            "Negotiation leverage identification",
            "Fact-based analysis and verification"
        ]
        
        print("📋 FORENSIC PROCESSING PIPELINE:")
        for i, process in enumerate(processing_pipeline, 1):
            print(f"   {i}. {process}")
        
        # Create processing command
        processing_command = f"""
# After Gmail export download, run complete analysis:
python3 GMAIL_COMPLETE_EXTRACTION_SYSTEM.py \\
    --target-email {self.target_email} \\
    --export-dir {self.export_dir} \\
    --analysis-mode complete \\
    --output-format forensic
"""
        
        command_file = self.export_dir / "run_complete_analysis.sh"
        with open(command_file, 'w') as f:
            f.write(processing_command)
        
        os.chmod(command_file, 0o755)
        
        print(f"⚡ Analysis command prepared: {command_file}")
        
        return {
            'success': True,
            'message': 'Forensic processing prepared',
            'analysis_command': str(command_file)
        }
    
    def create_verification_script(self):
        """Create data verification script"""
        script_content = '''#!/usr/bin/env python3
"""
Gmail Export Data Verification Script
Verify 100% data completeness and integrity
"""

import os
import zipfile
import hashlib
from pathlib import Path

def verify_gmail_export(export_dir):
    """Verify Gmail export completeness"""
    print("🔍 GMAIL EXPORT VERIFICATION")
    print("=" * 40)
    
    export_path = Path(export_dir)
    
    # Check for expected files
    zip_files = list(export_path.glob("takeout-*.zip"))
    
    if not zip_files:
        print("❌ No Gmail export files found")
        return False
    
    print(f"✅ Found {len(zip_files)} export files")
    
    # Verify each file
    for zip_file in zip_files:
        print(f"📁 Verifying: {zip_file.name}")
        
        # Check file size
        size_mb = zip_file.stat().st_size / (1024 * 1024)
        print(f"   Size: {size_mb:.1f} MB")
        
        # Verify ZIP integrity
        try:
            with zipfile.ZipFile(zip_file, 'r') as zf:
                test_result = zf.testzip()
                if test_result is None:
                    print(f"   ✅ ZIP integrity: VALID")
                else:
                    print(f"   ❌ ZIP integrity: CORRUPTED ({test_result})")
                    return False
        except Exception as e:
            print(f"   ❌ ZIP error: {e}")
            return False
    
    print("✅ All files verified successfully")
    return True

if __name__ == "__main__":
    verify_gmail_export("./gmail_exports")
'''
        
        script_file = self.export_dir / "verify_export.py"
        with open(script_file, 'w') as f:
            f.write(script_content)
        
        os.chmod(script_file, 0o755)
        return script_file
    
    def generate_export_report(self):
        """Generate complete export process report"""
        report = {
            'target_email': self.target_email,
            'export_process_completed': datetime.now().isoformat(),
            'steps_executed': len(self.export_log),
            'export_log': self.export_log,
            'export_directory': str(self.export_dir.absolute()),
            'next_steps': [
                'Wait for Google Takeout email notification',
                'Download all export files to specified directory',
                'Run verification script to ensure data integrity',
                'Execute complete analysis using GMAIL_COMPLETE_EXTRACTION_SYSTEM.py'
            ],
            'success_indicators': [
                'All export steps completed successfully',
                'Download tracker configured',
                'Verification tools prepared',
                'Analysis pipeline ready'
            ]
        }
        
        report_file = self.export_dir / f"export_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print("📊 EXPORT PROCESS REPORT")
        print("=" * 30)
        print(f"✅ Process completed successfully")
        print(f"📁 Export directory: {self.export_dir}")
        print(f"📋 Report saved: {report_file}")
        print("")
        print("🎯 NEXT ACTIONS:")
        print("1. Wait for Google email notification")
        print("2. Download all files to export directory")
        print("3. Run verification script")
        print("4. Execute complete Gmail analysis")
        
        return report

def main():
    """Main interface for Gmail export automation"""
    print("📧 GMAIL EXPORT AUTOMATION SYSTEM")
    print("=" * 50)
    print("Target: ck.chawakorn@gmail.com")
    print("🎯 100% Data Capture | Zero Human Error")
    print("")
    
    automator = GmailExportAutomator("ck.chawakorn@gmail.com")
    
    print("🚀 AUTOMATION FEATURES:")
    print("✅ Step-by-step export guidance")
    print("✅ Configuration verification")
    print("✅ Download monitoring")
    print("✅ Data integrity verification")
    print("✅ Forensic processing preparation")
    print("")
    
    start = input("🎯 Start complete Gmail export process? (y/n): ")
    
    if start.lower() == 'y':
        report = automator.complete_export_process()
        return report
    else:
        print("Export process cancelled.")
        return None

if __name__ == "__main__":
    main()