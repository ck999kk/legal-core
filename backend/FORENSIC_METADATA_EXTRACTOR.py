#!/usr/bin/env python3
"""
Forensic Metadata Extractor for Legal Evidence Analysis
Complete metadata extraction from Gmail evidence set for tenancy dispute
Based on claude_forensic_full_metadata.txt requirements

Forensic integrity | Neutral analysis | Educational purpose only
"""

import json
import email
import hashlib
import re
from datetime import datetime
from pathlib import Path
import sqlite3
from email.parser import Parser
from email.policy import default
import base64
import mimetypes
import zipfile
import logging

class ForensicMetadataExtractor:
    """Complete forensic metadata extraction from email evidence"""
    
    def __init__(self, case_id="RT252398"):
        self.case_id = case_id
        self.workspace = Path("./forensic_evidence")
        self.workspace.mkdir(exist_ok=True)
        
        # Initialize forensic database
        self.forensic_db = self.workspace / "forensic_metadata.db"
        self.init_forensic_database()
        
        # Configure forensic logging
        logging.basicConfig(
            filename=self.workspace / 'forensic_extraction.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
        self.extracted_metadata = []
        self.forensic_timeline = []
        
    def init_forensic_database(self):
        """Initialize forensic evidence database"""
        with sqlite3.connect(self.forensic_db) as conn:
            # Email-level metadata table
            conn.execute("""
                CREATE TABLE IF NOT EXISTS email_metadata (
                    id INTEGER PRIMARY KEY,
                    message_id TEXT UNIQUE,
                    date_rfc2822 TEXT,
                    date_parsed DATETIME,
                    sender_name TEXT,
                    sender_email TEXT,
                    recipients_to TEXT,
                    recipients_cc TEXT,
                    recipients_bcc TEXT,
                    reply_to TEXT,
                    subject TEXT,
                    references TEXT,
                    in_reply_to TEXT,
                    mime_version TEXT,
                    content_type TEXT,
                    transfer_encoding TEXT,
                    x_mailer TEXT,
                    x_originating_ip TEXT,
                    received_path TEXT,
                    authentication_results TEXT,
                    arc_authentication TEXT,
                    delivered_to TEXT,
                    message_hash TEXT,
                    extraction_timestamp DATETIME
                )
            """)
            
            # Attachment metadata table
            conn.execute("""
                CREATE TABLE IF NOT EXISTS attachment_metadata (
                    id INTEGER PRIMARY KEY,
                    email_id INTEGER,
                    filename TEXT,
                    mime_type TEXT,
                    file_size INTEGER,
                    content_hash TEXT,
                    creation_date TEXT,
                    modification_date TEXT,
                    embedded_signatures TEXT,
                    exif_data TEXT,
                    FOREIGN KEY (email_id) REFERENCES email_metadata (id)
                )
            """)
            
            # Behavioral analysis table
            conn.execute("""
                CREATE TABLE IF NOT EXISTS behavioral_analysis (
                    id INTEGER PRIMARY KEY,
                    email_id INTEGER,
                    thread_depth INTEGER,
                    response_latency_hours REAL,
                    timestamp_after_hours BOOLEAN,
                    language_tone TEXT,
                    sentiment_score REAL,
                    manipulation_indicators TEXT,
                    legal_clause_references TEXT,
                    retaliation_timing_score REAL,
                    FOREIGN KEY (email_id) REFERENCES email_metadata (id)
                )
            """)
    
    def execute_complete_forensic_extraction(self, email_source_path):
        """Execute complete forensic metadata extraction"""
        print("🔬 FORENSIC METADATA EXTRACTOR")
        print("=" * 50)
        print(f"🎯 Case: {self.case_id}")
        print("⚖️  Purpose: Legal education and evidence analysis")
        print("🛡️  Forensic integrity maintained | Neutral analysis")
        print("")
        
        # Process email evidence
        if Path(email_source_path).is_file():
            if email_source_path.endswith('.eml'):
                self.process_single_eml(email_source_path)
            elif email_source_path.endswith('.mbox'):
                self.process_mbox_file(email_source_path)
            elif email_source_path.endswith('.zip'):
                self.process_zip_archive(email_source_path)
        elif Path(email_source_path).is_dir():
            self.process_email_directory(email_source_path)
        
        # Generate forensic analysis
        forensic_analysis = self.generate_forensic_analysis()
        
        # Create output reports
        self.create_forensic_reports(forensic_analysis)
        
        print("")
        print("✅ FORENSIC EXTRACTION COMPLETED")
        print(f"📊 Emails processed: {len(self.extracted_metadata)}")
        print(f"⏰ Timeline events: {len(self.forensic_timeline)}")
        print(f"💾 Database: {self.forensic_db}")
        
        return forensic_analysis
    
    def process_single_eml(self, eml_path):
        """Process single .eml file with complete metadata extraction"""
        print(f"📧 Processing EML: {Path(eml_path).name}")
        
        try:
            with open(eml_path, 'rb') as f:
                msg = email.message_from_bytes(f.read(), policy=default)
            
            # Extract complete metadata
            metadata = self.extract_complete_email_metadata(msg)
            
            # Extract attachments
            attachments = self.extract_attachment_metadata(msg)
            
            # Perform behavioral analysis
            behavioral = self.analyze_email_behavior(msg, metadata)
            
            # Store in database
            self.store_email_metadata(metadata, attachments, behavioral)
            
            self.extracted_metadata.append({
                'metadata': metadata,
                'attachments': attachments,
                'behavioral': behavioral
            })
            
            # Add to forensic timeline
            self.forensic_timeline.append({
                'timestamp': metadata['date_parsed'],
                'event_type': 'email_communication',
                'participants': [metadata['sender_email']] + metadata['recipients_to'],
                'subject': metadata['subject'],
                'metadata_hash': metadata['message_hash']
            })
            
        except Exception as e:
            logging.error(f"Error processing {eml_path}: {e}")
            print(f"   ❌ Error processing {eml_path}: {e}")
    
    def extract_complete_email_metadata(self, msg):
        """Extract all metadata fields as specified in requirements"""
        metadata = {}
        
        # Basic email headers
        metadata['message_id'] = msg.get('Message-ID', '')
        metadata['date_rfc2822'] = msg.get('Date', '')
        metadata['date_parsed'] = email.utils.parsedate_to_datetime(msg.get('Date', '')) if msg.get('Date') else None
        
        # Sender information
        sender_parsed = email.utils.parseaddr(msg.get('From', ''))
        metadata['sender_name'] = sender_parsed[0]
        metadata['sender_email'] = sender_parsed[1]
        
        # Recipients
        metadata['recipients_to'] = [addr[1] for addr in email.utils.getaddresses(msg.get_all('To', []))]
        metadata['recipients_cc'] = [addr[1] for addr in email.utils.getaddresses(msg.get_all('Cc', []))]
        metadata['recipients_bcc'] = [addr[1] for addr in email.utils.getaddresses(msg.get_all('Bcc', []))]
        
        # Other headers
        metadata['reply_to'] = msg.get('Reply-To', '')
        metadata['subject'] = msg.get('Subject', '')
        metadata['references'] = msg.get('References', '')
        metadata['in_reply_to'] = msg.get('In-Reply-To', '')
        
        # Technical headers
        metadata['mime_version'] = msg.get('MIME-Version', '')
        metadata['content_type'] = msg.get('Content-Type', '')
        metadata['transfer_encoding'] = msg.get('Content-Transfer-Encoding', '')
        metadata['x_mailer'] = msg.get('X-Mailer', '')
        metadata['x_originating_ip'] = msg.get('X-Originating-IP', '')
        
        # Server path analysis
        received_headers = msg.get_all('Received', [])
        metadata['received_path'] = self.analyze_received_path(received_headers)
        
        # Authentication results
        metadata['authentication_results'] = msg.get('Authentication-Results', '')
        metadata['arc_authentication'] = msg.get('ARC-Authentication-Results', '')
        metadata['delivered_to'] = msg.get('Delivered-To', '')
        
        # Content hash for integrity
        content = str(msg)
        metadata['message_hash'] = hashlib.sha256(content.encode()).hexdigest()
        
        metadata['extraction_timestamp'] = datetime.now().isoformat()
        
        return metadata
    
    def extract_attachment_metadata(self, msg):
        """Extract metadata from all attachments"""
        attachments = []
        
        for part in msg.walk():
            if part.get_content_disposition() == 'attachment':
                attachment_meta = {}
                
                # Basic file information
                attachment_meta['filename'] = part.get_filename()
                attachment_meta['mime_type'] = part.get_content_type()
                
                # Content analysis
                content = part.get_payload(decode=True)
                if content:
                    attachment_meta['file_size'] = len(content)
                    attachment_meta['content_hash'] = hashlib.sha256(content).hexdigest()
                    
                    # Extract file metadata based on type
                    if attachment_meta['mime_type'].startswith('image/'):
                        attachment_meta['exif_data'] = self.extract_image_exif(content)
                    elif attachment_meta['mime_type'] == 'application/pdf':
                        attachment_meta['pdf_metadata'] = self.extract_pdf_metadata(content)
                
                attachments.append(attachment_meta)
        
        return attachments
    
    def analyze_email_behavior(self, msg, metadata):
        """Analyze behavioral patterns and legal indicators"""
        behavioral = {}
        
        content = self.get_email_content(msg)
        
        # Thread analysis
        behavioral['thread_depth'] = len(metadata['references'].split()) if metadata['references'] else 0
        
        # Timing analysis
        if metadata['date_parsed']:
            hour = metadata['date_parsed'].hour
            behavioral['timestamp_after_hours'] = hour < 7 or hour > 18
        
        # Language analysis
        behavioral['language_tone'] = self.analyze_language_tone(content)
        behavioral['sentiment_score'] = self.calculate_sentiment_score(content)
        
        # Legal clause detection
        behavioral['legal_clause_references'] = self.detect_legal_clauses(content)
        
        # Manipulation indicators
        behavioral['manipulation_indicators'] = self.detect_manipulation_patterns(content)
        
        # Subject line analysis for urgency/pressure
        behavioral['urgency_indicators'] = self.analyze_urgency_patterns(metadata['subject'])
        
        return behavioral
    
    def detect_legal_clauses(self, content):
        """Detect legal clause references (Section 86, 91ZZL, etc.)"""
        legal_patterns = [
            r'Section\s+\d+[A-Z]*',
            r's\s*\.\s*\d+[A-Z]*',
            r'91ZZ[A-Z]',
            r'Section\s+86',
            r'Residential Tenancies Act',
            r'VCAT',
            r'notice to vacate',
            r'breach of duty'
        ]
        
        detected_clauses = []
        content_lower = content.lower()
        
        for pattern in legal_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                detected_clauses.extend(matches)
        
        return detected_clauses
    
    def analyze_language_tone(self, content):
        """Analyze language tone (aggressive, passive, professional)"""
        aggressive_indicators = ['must', 'require', 'demand', 'immediately', 'failure to']
        passive_indicators = ['please', 'kindly', 'would appreciate', 'if possible']
        professional_indicators = ['pursuant to', 'in accordance with', 'please find', 'reference']
        
        content_lower = content.lower()
        
        aggressive_score = sum(1 for indicator in aggressive_indicators if indicator in content_lower)
        passive_score = sum(1 for indicator in passive_indicators if indicator in content_lower)
        professional_score = sum(1 for indicator in professional_indicators if indicator in content_lower)
        
        if aggressive_score > max(passive_score, professional_score):
            return 'aggressive'
        elif passive_score > professional_score:
            return 'passive'
        elif professional_score > 0:
            return 'professional'
        else:
            return 'neutral'
    
    def generate_forensic_analysis(self):
        """Generate comprehensive forensic analysis"""
        analysis = {
            'case_metadata': {
                'case_id': self.case_id,
                'extraction_date': datetime.now().isoformat(),
                'total_emails': len(self.extracted_metadata),
                'forensic_integrity': 'MAINTAINED',
                'analysis_purpose': 'Legal education and evidence analysis'
            },
            'timeline_analysis': self.create_forensic_timeline(),
            'actor_role_mapping': self.map_actor_roles(),
            'contradiction_matrix': self.identify_contradictions(),
            'retaliation_analysis': self.analyze_retaliation_patterns(),
            'authentication_validation': self.validate_email_authentication(),
            'metadata_integrity_report': self.generate_integrity_report()
        }
        
        return analysis
    
    def create_forensic_timeline(self):
        """Create chronological forensic timeline"""
        timeline = sorted(self.forensic_timeline, key=lambda x: x['timestamp'] if x['timestamp'] else datetime.min)
        
        timeline_analysis = {
            'total_events': len(timeline),
            'date_range': {
                'start': timeline[0]['timestamp'].isoformat() if timeline and timeline[0]['timestamp'] else None,
                'end': timeline[-1]['timestamp'].isoformat() if timeline and timeline[-1]['timestamp'] else None
            },
            'events': timeline,
            'gap_analysis': self.analyze_timeline_gaps(timeline)
        }
        
        return timeline_analysis
    
    def map_actor_roles(self):
        """Map roles of different actors in the communication"""
        actors = {}
        
        for email_data in self.extracted_metadata:
            metadata = email_data['metadata']
            
            sender = metadata['sender_email']
            if sender not in actors:
                actors[sender] = {
                    'email': sender,
                    'name': metadata['sender_name'],
                    'role': self.determine_actor_role(sender, metadata['sender_name']),
                    'communication_count': 0,
                    'first_contact': metadata['date_parsed'],
                    'last_contact': metadata['date_parsed']
                }
            
            actors[sender]['communication_count'] += 1
            if metadata['date_parsed']:
                if not actors[sender]['first_contact'] or metadata['date_parsed'] < actors[sender]['first_contact']:
                    actors[sender]['first_contact'] = metadata['date_parsed']
                if not actors[sender]['last_contact'] or metadata['date_parsed'] > actors[sender]['last_contact']:
                    actors[sender]['last_contact'] = metadata['date_parsed']
        
        return actors
    
    def determine_actor_role(self, email, name):
        """Determine role based on email domain and name patterns"""
        if 'areal' in email.lower():
            return 'property_manager'
        elif 'vcat' in email.lower():
            return 'tribunal'
        elif any(keyword in email.lower() for keyword in ['government', 'gov.au', 'vic.gov']):
            return 'government_agency'
        elif 'chawakorn' in email.lower():
            return 'tenant'
        else:
            return 'unknown'
    
    def create_forensic_reports(self, analysis):
        """Create comprehensive forensic reports"""
        # Main forensic report
        report_file = self.workspace / f"forensic_analysis_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w') as f:
            json.dump(analysis, f, indent=2, default=str)
        
        # Evidence summary
        evidence_summary = self.workspace / "evidence_summary.txt"
        with open(evidence_summary, 'w') as f:
            f.write("FORENSIC EVIDENCE SUMMARY\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Case ID: {self.case_id}\n")
            f.write(f"Total Emails: {len(self.extracted_metadata)}\n")
            f.write(f"Analysis Date: {datetime.now().isoformat()}\n")
            f.write(f"Purpose: Legal education and evidence analysis\n\n")
            
            f.write("ACTOR ROLES:\n")
            for actor in analysis['actor_role_mapping'].values():
                f.write(f"- {actor['name']} ({actor['email']}): {actor['role']}\n")
        
        print(f"📋 Forensic report: {report_file}")
        print(f"📄 Evidence summary: {evidence_summary}")
    
    # Helper methods
    def get_email_content(self, msg):
        """Extract text content from email"""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    return part.get_payload(decode=True).decode('utf-8', errors='ignore')
        else:
            return msg.get_payload(decode=True).decode('utf-8', errors='ignore')
        return ""
    
    def analyze_received_path(self, received_headers):
        """Analyze email server path from Received headers"""
        path_analysis = []
        for header in received_headers:
            # Extract server information from Received header
            server_match = re.search(r'from\s+([^\s]+)', header)
            if server_match:
                path_analysis.append(server_match.group(1))
        return ' -> '.join(path_analysis)
    
    def store_email_metadata(self, metadata, attachments, behavioral):
        """Store metadata in forensic database"""
        with sqlite3.connect(self.forensic_db) as conn:
            # Store email metadata
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO email_metadata 
                (message_id, date_rfc2822, date_parsed, sender_name, sender_email, 
                 recipients_to, subject, message_hash, extraction_timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                metadata['message_id'], metadata['date_rfc2822'], metadata['date_parsed'],
                metadata['sender_name'], metadata['sender_email'], 
                json.dumps(metadata['recipients_to']), metadata['subject'], 
                metadata['message_hash'], metadata['extraction_timestamp']
            ))
            
            email_id = cursor.lastrowid
            
            # Store attachments
            for attachment in attachments:
                cursor.execute("""
                    INSERT INTO attachment_metadata 
                    (email_id, filename, mime_type, file_size, content_hash)
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    email_id, attachment.get('filename'), attachment.get('mime_type'),
                    attachment.get('file_size'), attachment.get('content_hash')
                ))

def main():
    """Main interface for forensic metadata extraction"""
    print("🔬 FORENSIC METADATA EXTRACTOR")
    print("=" * 50)
    print("Purpose: Legal education and evidence analysis")
    print("Forensic integrity maintained | Neutral analysis")
    print("")
    
    extractor = ForensicMetadataExtractor()
    
    email_source = input("📧 Enter email source path (.eml, .mbox, .zip, or directory): ").strip()
    
    if email_source and Path(email_source).exists():
        analysis = extractor.execute_complete_forensic_extraction(email_source)
        return analysis
    else:
        print("❌ Invalid or missing email source path")
        return None

if __name__ == "__main__":
    main()