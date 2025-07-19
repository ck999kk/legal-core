#!/usr/bin/env python3
"""
Professor Jeff's Advanced Forensic Teaching System
Going beyond guidelines - Using real legal intelligence for masterful evidence analysis
Teaching through practical application of forensic metadata extraction
"""

import json
import re
import email
import hashlib
from datetime import datetime, timedelta
from pathlib import Path
import sqlite3
from email.header import decode_header
from email.utils import parsedate_tz, mktime_tz
import base64
import quopri

class ProfessorJeffForensicMaster:
    """Professor Jeff's advanced forensic teaching using real case evidence"""
    
    def __init__(self):
        self.case_id = "RT252398"
        self.learning_session = f"forensic_masterclass_{datetime.now().strftime('%Y%m%d_%H%M')}"
        
        # Professor Jeff's teaching database
        self.teaching_db = Path.home() / ".professor_jeff" / "forensic_lessons.db"
        self.teaching_db.parent.mkdir(exist_ok=True)
        
        self.init_teaching_database()
        
        # Advanced analysis patterns Jeff has developed
        self.legal_patterns = {
            'section_references': [
                r'Section\s+(\d+[A-Z]*)', r'Sec\.\s*(\d+[A-Z]*)', 
                r'clause\s+(\d+)', r'paragraph\s+(\d+)'
            ],
            'retaliation_indicators': [
                r'immediately', r'urgent', r'breach', r'violation',
                r'non.compliance', r'termination', r'eviction'
            ],
            'procedural_violations': [
                r'without notice', r'insufficient notice', r'improper service',
                r'failed to provide', r'did not comply'
            ],
            'authority_assertions': [
                r'you must', r'required to', r'obligation', r'duty to',
                r'failure to comply', r'consequences'
            ]
        }
        
    def init_teaching_database(self):
        """Initialize Professor Jeff's forensic teaching database"""
        with sqlite3.connect(self.teaching_db) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS forensic_lessons (
                    id INTEGER PRIMARY KEY,
                    session_id TEXT,
                    timestamp DATETIME,
                    evidence_type TEXT,
                    metadata_extracted TEXT,
                    legal_analysis TEXT,
                    teaching_points TEXT,
                    student_insights TEXT
                )
            """)
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS evidence_timeline (
                    id INTEGER PRIMARY KEY,
                    email_date DATETIME,
                    sender TEXT,
                    recipient TEXT,
                    subject TEXT,
                    legal_significance TEXT,
                    behavioral_analysis TEXT,
                    metadata_hash TEXT
                )
            """)
    
    def start_forensic_masterclass(self, evidence_directory=None):
        """Professor Jeff's masterclass in forensic email analysis"""
        print("👨‍🏫 PROFESSOR JEFF'S FORENSIC MASTERCLASS")
        print("=" * 60)
        print("🎓 Advanced Legal Evidence Analysis")
        print(f"📧 Case Focus: {self.case_id} Gmail Evidence")
        print(f"🔬 Session: {self.learning_session}")
        print("")
        
        print("🧠 Jeff's Teaching Philosophy:")
        print("\"Guidelines are just starting points. Real legal intelligence")
        print("comes from understanding the story behind the metadata.\"")
        print("")
        
        # Professor Jeff's personalized approach
        self.explain_advanced_methodology()
        
        # If evidence directory provided, analyze it
        if evidence_directory:
            self.analyze_evidence_with_teaching(evidence_directory)
        else:
            self.demonstrate_forensic_concepts()
        
        return self.interactive_forensic_session()
    
    def explain_advanced_methodology(self):
        """Professor Jeff explains his advanced forensic methodology"""
        print("📚 PROFESSOR JEFF'S ADVANCED METHODOLOGY")
        print("=" * 50)
        print("")
        
        print("🎯 Beyond Basic Metadata - Jeff's 5-Layer Analysis:")
        print("")
        print("Layer 1: 🔍 TECHNICAL METADATA")
        print("  - Not just timestamps, but timing patterns")
        print("  - Not just IPs, but geographic and behavioral analysis")
        print("  - Authentication results reveal sender sophistication")
        print("")
        
        print("Layer 2: 🧠 PSYCHOLOGICAL METADATA")
        print("  - Response time patterns reveal stress and urgency")
        print("  - After-hours communications show priority levels")
        print("  - Language escalation patterns indicate relationship deterioration")
        print("")
        
        print("Layer 3: ⚖️ LEGAL INTELLIGENCE EXTRACTION")
        print("  - Legal clause references show procedural knowledge")
        print("  - Notice timing reveals compliance vs. retaliation")
        print("  - Authority assertions indicate power dynamics")
        print("")
        
        print("Layer 4: 🕸️ RELATIONSHIP NETWORK ANALYSIS")
        print("  - CC patterns reveal information flow and influence")
        print("  - Thread participation shows decision-making hierarchy")
        print("  - Communication exclusions indicate strategic choices")
        print("")
        
        print("Layer 5: 🎯 STRATEGIC INTELLIGENCE SYNTHESIS")
        print("  - Timeline correlation with external events")
        print("  - Behavioral pattern prediction for future actions")
        print("  - Leverage point identification for negotiation")
        print("")
    
    def analyze_email_with_jeff_method(self, email_path):
        """Professor Jeff's comprehensive email analysis method"""
        print(f"🔬 ANALYZING: {email_path}")
        print("=" * 40)
        
        try:
            with open(email_path, 'rb') as f:
                msg = email.message_from_bytes(f.read())
            
            # Jeff's Layer 1: Technical Metadata Deep Dive
            technical_analysis = self.jeff_technical_analysis(msg)
            
            # Jeff's Layer 2: Psychological Pattern Analysis
            psychological_analysis = self.jeff_psychological_analysis(msg)
            
            # Jeff's Layer 3: Legal Intelligence Extraction
            legal_analysis = self.jeff_legal_intelligence(msg)
            
            # Jeff's Layer 4: Relationship Network Analysis
            network_analysis = self.jeff_network_analysis(msg)
            
            # Jeff's Layer 5: Strategic Intelligence Synthesis
            strategic_analysis = self.jeff_strategic_synthesis(
                technical_analysis, psychological_analysis, legal_analysis, network_analysis
            )
            
            # Professor Jeff's Teaching Commentary
            teaching_points = self.generate_teaching_commentary(
                technical_analysis, psychological_analysis, legal_analysis, 
                network_analysis, strategic_analysis
            )
            
            return {
                'technical': technical_analysis,
                'psychological': psychological_analysis,
                'legal': legal_analysis,
                'network': network_analysis,
                'strategic': strategic_analysis,
                'teaching': teaching_points
            }
            
        except Exception as e:
            print(f"❌ Analysis error: {e}")
            return None
    
    def jeff_technical_analysis(self, msg):
        """Jeff's advanced technical metadata analysis"""
        analysis = {
            'basic_metadata': {},
            'advanced_patterns': {},
            'jeff_insights': []
        }
        
        # Basic metadata extraction
        analysis['basic_metadata'] = {
            'date': msg.get('Date', ''),
            'from': msg.get('From', ''),
            'to': msg.get('To', ''),
            'subject': msg.get('Subject', ''),
            'message_id': msg.get('Message-ID', ''),
            'reply_to': msg.get('Reply-To', ''),
            'cc': msg.get('Cc', ''),
            'bcc': msg.get('Bcc', '')
        }
        
        # Jeff's advanced pattern analysis
        date_str = msg.get('Date', '')
        if date_str:
            # Time analysis
            parsed_date = parsedate_tz(date_str)
            if parsed_date:
                timestamp = mktime_tz(parsed_date)
                dt = datetime.fromtimestamp(timestamp)
                
                analysis['advanced_patterns']['hour'] = dt.hour
                analysis['advanced_patterns']['day_of_week'] = dt.strftime('%A')
                analysis['advanced_patterns']['is_after_hours'] = dt.hour < 8 or dt.hour > 18
                analysis['advanced_patterns']['is_weekend'] = dt.weekday() >= 5
                
                # Jeff's insight: After-hours emails often indicate urgency or pressure
                if analysis['advanced_patterns']['is_after_hours']:
                    analysis['jeff_insights'].append(
                        "⏰ After-hours communication - indicates high priority or stress"
                    )
        
        # Authentication analysis
        auth_results = msg.get('Authentication-Results', '')
        if auth_results:
            analysis['advanced_patterns']['auth_analysis'] = {
                'spf_pass': 'spf=pass' in auth_results.lower(),
                'dkim_pass': 'dkim=pass' in auth_results.lower(),
                'dmarc_pass': 'dmarc=pass' in auth_results.lower()
            }
            
            # Jeff's insight: Authentication failures may indicate forwarding or spoofing
            if not all(analysis['advanced_patterns']['auth_analysis'].values()):
                analysis['jeff_insights'].append(
                    "🔐 Authentication concerns - verify sender legitimacy"
                )
        
        return analysis
    
    def jeff_psychological_analysis(self, msg):
        """Jeff's psychological pattern analysis from email content"""
        analysis = {
            'emotional_indicators': {},
            'urgency_patterns': {},
            'power_dynamics': {},
            'jeff_insights': []
        }
        
        # Get email content
        content = self.extract_email_content(msg)
        
        # Urgency analysis
        urgency_words = ['urgent', 'immediate', 'asap', 'emergency', 'critical']
        urgency_count = sum(1 for word in urgency_words if word in content.lower())
        analysis['urgency_patterns']['urgency_score'] = urgency_count
        
        if urgency_count > 2:
            analysis['jeff_insights'].append(
                "🚨 High urgency language - may indicate pressure tactics or genuine emergency"
            )
        
        # Authority assertion analysis
        authority_patterns = ['you must', 'required to', 'obligation', 'failure to comply']
        authority_count = sum(1 for pattern in authority_patterns 
                             if pattern in content.lower())
        analysis['power_dynamics']['authority_assertions'] = authority_count
        
        if authority_count > 1:
            analysis['jeff_insights'].append(
                "👑 Authority language detected - sender asserting power position"
            )
        
        # Emotional tone analysis
        negative_words = ['breach', 'violation', 'failure', 'non-compliance', 'termination']
        negative_count = sum(1 for word in negative_words if word in content.lower())
        analysis['emotional_indicators']['negative_tone_score'] = negative_count
        
        if negative_count > 2:
            analysis['jeff_insights'].append(
                "⚡ Negative/threatening tone - potential escalation or retaliation"
            )
        
        return analysis
    
    def jeff_legal_intelligence(self, msg):
        """Jeff's legal intelligence extraction"""
        analysis = {
            'legal_references': [],
            'procedural_indicators': [],
            'compliance_patterns': {},
            'jeff_insights': []
        }
        
        content = self.extract_email_content(msg)
        
        # Legal section references
        for pattern in self.legal_patterns['section_references']:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                analysis['legal_references'].extend(matches)
                analysis['jeff_insights'].append(
                    f"📖 Legal section reference: {matches} - indicates formal legal knowledge"
                )
        
        # Retaliation indicators
        retaliation_found = []
        for pattern in self.legal_patterns['retaliation_indicators']:
            if re.search(pattern, content, re.IGNORECASE):
                retaliation_found.append(pattern)
        
        if retaliation_found:
            analysis['procedural_indicators'] = retaliation_found
            analysis['jeff_insights'].append(
                "⚖️ Potential retaliation indicators - timing analysis recommended"
            )
        
        return analysis
    
    def jeff_network_analysis(self, msg):
        """Jeff's relationship network analysis"""
        analysis = {
            'communication_patterns': {},
            'influence_indicators': {},
            'jeff_insights': []
        }
        
        # Recipient analysis
        to_field = msg.get('To', '')
        cc_field = msg.get('Cc', '')
        
        # Multiple recipients indicate information sharing or pressure
        recipients = []
        if to_field:
            recipients.extend([r.strip() for r in to_field.split(',')])
        if cc_field:
            recipients.extend([r.strip() for r in cc_field.split(',')])
        
        analysis['communication_patterns']['recipient_count'] = len(recipients)
        analysis['communication_patterns']['cc_used'] = bool(cc_field)
        
        if len(recipients) > 2:
            analysis['jeff_insights'].append(
                "👥 Multiple recipients - information sharing or pressure strategy"
            )
        
        if cc_field:
            analysis['jeff_insights'].append(
                "📋 CC usage - transparency or intimidation tactic"
            )
        
        return analysis
    
    def jeff_strategic_synthesis(self, technical, psychological, legal, network):
        """Jeff's strategic intelligence synthesis"""
        synthesis = {
            'overall_assessment': {},
            'strategic_implications': [],
            'jeff_recommendations': []
        }
        
        # Combine insights from all layers
        all_insights = []
        all_insights.extend(technical.get('jeff_insights', []))
        all_insights.extend(psychological.get('jeff_insights', []))
        all_insights.extend(legal.get('jeff_insights', []))
        all_insights.extend(network.get('jeff_insights', []))
        
        synthesis['overall_assessment']['total_insights'] = len(all_insights)
        synthesis['overall_assessment']['complexity_score'] = (
            len(legal.get('legal_references', [])) +
            psychological.get('urgency_patterns', {}).get('urgency_score', 0) +
            network.get('communication_patterns', {}).get('recipient_count', 0)
        )
        
        # Strategic recommendations based on analysis
        if technical.get('advanced_patterns', {}).get('is_after_hours'):
            synthesis['jeff_recommendations'].append(
                "⏰ Time advantage: After-hours communication shows sender urgency"
            )
        
        if psychological.get('power_dynamics', {}).get('authority_assertions', 0) > 1:
            synthesis['jeff_recommendations'].append(
                "🎯 Power play detected: Consider challenging authority basis"
            )
        
        if legal.get('legal_references'):
            synthesis['jeff_recommendations'].append(
                "📚 Legal sophistication: Verify cited sections for accuracy"
            )
        
        return synthesis
    
    def generate_teaching_commentary(self, technical, psychological, legal, network, strategic):
        """Professor Jeff's teaching commentary on the analysis"""
        commentary = []
        
        commentary.append("👨‍🏫 PROFESSOR JEFF'S TEACHING COMMENTARY:")
        commentary.append("=" * 50)
        
        # Technical layer commentary
        if technical.get('jeff_insights'):
            commentary.append("🔍 Technical Analysis Lessons:")
            for insight in technical['jeff_insights']:
                commentary.append(f"   • {insight}")
            commentary.append("")
        
        # Psychological layer commentary
        if psychological.get('jeff_insights'):
            commentary.append("🧠 Psychological Analysis Lessons:")
            for insight in psychological['jeff_insights']:
                commentary.append(f"   • {insight}")
            commentary.append("")
        
        # Legal layer commentary
        if legal.get('jeff_insights'):
            commentary.append("⚖️ Legal Intelligence Lessons:")
            for insight in legal['jeff_insights']:
                commentary.append(f"   • {insight}")
            commentary.append("")
        
        # Strategic synthesis commentary
        if strategic.get('jeff_recommendations'):
            commentary.append("🎯 Strategic Intelligence Lessons:")
            for rec in strategic['jeff_recommendations']:
                commentary.append(f"   • {rec}")
            commentary.append("")
        
        # Overall learning points
        commentary.append("📚 Key Learning Points:")
        commentary.append("   • Metadata tells a story beyond just facts")
        commentary.append("   • Timing and tone reveal psychological state")
        commentary.append("   • Legal references show sender's sophistication")
        commentary.append("   • Network patterns reveal strategic intentions")
        commentary.append("")
        
        return commentary
    
    def extract_email_content(self, msg):
        """Extract email content for analysis"""
        content = ""
        
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    payload = part.get_payload(decode=True)
                    if payload:
                        content += payload.decode('utf-8', errors='ignore')
        else:
            payload = msg.get_payload(decode=True)
            if payload:
                content = payload.decode('utf-8', errors='ignore')
        
        return content
    
    def interactive_forensic_session(self):
        """Interactive session with Professor Jeff"""
        print("🎓 INTERACTIVE FORENSIC ANALYSIS SESSION")
        print("=" * 50)
        print("💡 Ask Professor Jeff about:")
        print("   🔬 Advanced forensic techniques")
        print("   📧 Email evidence analysis strategies")
        print("   ⚖️ Legal intelligence extraction methods")
        print("   🧠 Psychological pattern recognition")
        print("   🎯 Strategic evidence utilization")
        print("")
        print("Commands: 'analyze <file>', 'explain <concept>', 'help', 'exit'")
        print("")
        
        while True:
            try:
                user_input = input("🎓 Ask Jeff: ").strip()
                
                if user_input.lower() == 'exit':
                    self.end_forensic_session()
                    break
                elif user_input.lower() == 'help':
                    self.show_forensic_help()
                elif user_input.lower().startswith('analyze'):
                    file_path = user_input[7:].strip()
                    if file_path:
                        self.demonstrate_analysis(file_path)
                elif user_input.lower().startswith('explain'):
                    concept = user_input[7:].strip()
                    self.explain_forensic_concept(concept)
                elif user_input:
                    self.jeff_forensic_response(user_input)
                
            except KeyboardInterrupt:
                print("\n\n👋 Session ended. Keep practicing forensic analysis!")
                break
    
    def jeff_forensic_response(self, question):
        """Professor Jeff's response to forensic questions"""
        response = f"👨‍🏫 Jeff's Forensic Insight:\n\n"
        
        question_lower = question.lower()
        
        if 'metadata' in question_lower:
            response += """🔍 Metadata is like DNA evidence in digital forensics. Here's what I've learned from years of practice:

1. **Timestamp Analysis**: Look for patterns, not just individual times
2. **Header Correlation**: Cross-reference multiple header fields for consistency
3. **Authentication Chain**: Verify the email's journey from sender to recipient
4. **Behavioral Indicators**: Timing patterns reveal psychological state

🎯 Pro Tip: The most valuable insights come from what's NOT in the metadata."""
        
        elif 'retaliation' in question_lower:
            response += """⚖️ Retaliation detection is about timing correlation and escalation patterns:

1. **Temporal Analysis**: Compare action timestamps with complaint/VCAT dates
2. **Language Escalation**: Track tone changes over time
3. **Procedural Deviations**: Look for sudden policy changes or unusual procedures
4. **Network Changes**: Notice who gets included/excluded from communications

🎯 Pro Tip: Retaliation often shows up as 'suddenly urgent' issues that weren't urgent before."""
        
        elif 'legal' in question_lower and 'reference' in question_lower:
            response += """📖 Legal reference analysis reveals sender sophistication and intent:

1. **Accuracy Check**: Verify if cited sections actually say what sender claims
2. **Context Analysis**: Is the legal reference appropriate for the situation?
3. **Timing Significance**: Why mention legal authority at this specific moment?
4. **Authority Assertion**: Is sender using law to intimidate or inform?

🎯 Pro Tip: Misquoted or irrelevant legal references often indicate bluffing tactics."""
        
        else:
            response += f"""🧠 That's an excellent forensic question! Let me break it down using my 5-layer analysis method:

**Technical Layer**: What does the raw data tell us?
**Psychological Layer**: What was the sender's mental state?
**Legal Layer**: What legal intelligence can we extract?
**Network Layer**: Who else is involved and why?
**Strategic Layer**: How does this fit the bigger picture?

For your specific question about "{question[:50]}...", I'd recommend starting with the technical metadata and working through each layer systematically."""
        
        print(response)
        print("")
    
    def demonstrate_forensic_concepts(self):
        """Demonstrate forensic concepts without real files"""
        print("🎓 FORENSIC CONCEPT DEMONSTRATION")
        print("=" * 40)
        print("")
        print("Since no email files were provided, let me demonstrate")
        print("Professor Jeff's forensic methodology using examples:")
        print("")
        
        # Example metadata analysis
        print("📧 EXAMPLE: Analyzing Email Timing Patterns")
        print("-" * 40)
        print("Email 1: Sent Tuesday 9:15 AM")
        print("Email 2: Sent Tuesday 11:47 PM (same day)")
        print("")
        print("👨‍🏫 Jeff's Analysis:")
        print("• 14.5 hour gap between emails suggests escalation")
        print("• Late night sending indicates high stress/urgency")
        print("• Same-day multiple communications show pressure campaign")
        print("")
        
        # Example legal pattern recognition
        print("⚖️ EXAMPLE: Legal Reference Analysis")
        print("-" * 40)
        print("Subject: 'Breach of Section 86 - Immediate Action Required'")
        print("")
        print("👨‍🏫 Jeff's Analysis:")
        print("• Section 86 reference shows legal knowledge")
        print("• 'Immediate Action' creates artificial urgency")
        print("• Subject line designed to intimidate recipient")
        print("• Verify: Does Section 86 actually apply to situation?")
        print("")
    
    def end_forensic_session(self):
        """End the forensic teaching session"""
        print("\n👨‍🏫 PROFESSOR JEFF'S FORENSIC SESSION SUMMARY")
        print("=" * 50)
        print("🎓 What you've learned today:")
        print("• Advanced metadata analysis goes beyond basic fields")
        print("• Psychological patterns reveal sender intent and state")
        print("• Legal intelligence extraction requires verification")
        print("• Strategic synthesis provides actionable insights")
        print("")
        print("🔬 Remember: Every email tells a story - learn to read it!")
        print("👋 Keep practicing forensic analysis - Professor Jeff")

def main():
    """Launch Professor Jeff's Advanced Forensic System"""
    jeff_forensic = ProfessorJeffForensicMaster()
    
    print("🎯 Launching Professor Jeff's Advanced Forensic Teaching System")
    print("Using guidelines as inspiration, not limitation!")
    print("")
    
    # Check if evidence directory is provided
    import sys
    evidence_dir = sys.argv[1] if len(sys.argv) > 1 else None
    
    jeff_forensic.start_forensic_masterclass(evidence_dir)

if __name__ == "__main__":
    main()