import re
import sys

def process_file(filepath, chapter_num):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        
    out_lines = []
    
    for line in lines:
        s = line.rstrip('\n')
        
        # Heading fixes
        if chapter_num == 1:
            if s.startswith('## **1 '):
                s = s.replace('## **1 ', '# **1 ')
            elif s.startswith('### **1.'):
                s = s.replace('### **1.', '## **1.')
            elif s.startswith('#### **1.'):
                s = s.replace('#### **1.', '### **1.')
            elif s.startswith('#### Advantages'):
                s = '### Advantages'
            elif s.startswith('#### Disadvantages'):
                s = '### Disadvantages'
            elif s.startswith('#### Types of'):
                s = s.replace('#### Types of', '### Types of')
            elif s.startswith('#### **Android SDK**'):
                s = '### **Android SDK**'
            elif s.startswith('#### **Android Debug Bridge'):
                s = '### **Android Debug Bridge (ADB)**'
            elif s.startswith('#### **Android Developer Tools'):
                s = '### **Android Developer Tools and Android Studio**'
            elif s.startswith('#### **Dalvik Virtual Machine'):
                s = '### **Dalvik Virtual Machine (DVM)**'
            elif s.startswith('#### **Android RunTime'):
                s = '### **Android RunTime (ART)**'
        elif chapter_num in range(2, 9):
            m_chap = re.match(r'^\*\*Chapter (\d+) (.*)\*\*', s)
            if m_chap:
                s = f"# **{m_chap.group(1)} {m_chap.group(2)}**"
                
            m = re.match(r'^\*\*([2-8]) (.*)\*\*', s)
            if m:
                s = f"# **{m.group(1)} {m.group(2)}**"
            m2 = re.match(r'^\*\*([2-8]\.\d+) (.*)\*\*', s)
            if m2:
                s = f"## **{m2.group(1)} {m2.group(2)}**"
            m3 = re.match(r'^\*\*([2-8]\.\d+\.\d+) (.*)\*\*', s)
            if m3:
                s = f"### **{m3.group(1)} {m3.group(2)}**"
            
            # Subtitles without numbers but bolded like **Android Layout types**
            if s.startswith('**') and s.endswith('**') and not re.match(r'^#+ ', s):
                s = f"### {s}"

        # General prefix handler: => Prefix: Text
        # Except if it has Answer: in it
        m_qa = re.match(r'^=> Question (\d+): (.*?) Answer: (.*)$', s)
        if m_qa:
            s = f"=> **Question {m_qa.group(1)}**: `{m_qa.group(2)}` **Answer**: `{m_qa.group(3)}`"
        else:
            m_q_num = re.match(r'^=> Question (\d+):\s*(.*)$', s)
            if m_q_num:
                s = f"=> **Question {m_q_num.group(1)}**: `{m_q_num.group(2)}`"
            else:
                prefixes = ['Definition', 'Core concept', 'Important feature', 'Feature', 
                            'Example', 'Question', 'Answer', 'Important explanation point', 
                            'Limitation', 'Advantage', 'Characteristics', 'Advantages']
                
                for p in prefixes:
                    if s.startswith(f'=> {p}:'):
                        s = s.replace(f'=> {p}: ', f'=> **{p}**: `') + '`'
                    elif s.startswith(f'=> **{p}**: `'):
                        pass

        # List items formatting: "1. Term: Definition"
        m_list = re.match(r'^(\d+\.)\s+([^:]+):\s(.*)$', s)
        if m_list:
            term = m_list.group(2)
            # If term looks like code, use backticks
            if '.' in term or '(' in term or (term.islower() and not ' ' in term and term not in ['yes', 'no']):
                term = term.replace('`', '')
                s = f"{m_list.group(1)} `{term}`: {m_list.group(3)}"
            else:
                term = term.replace('**', '')
                s = f"{m_list.group(1)} **{term}**: {m_list.group(3)}"

        out_lines.append(s)

    with open(filepath, 'w') as f:
        f.write('\n'.join(out_lines) + '\n')
        
    print(f"Processed chapter {chapter_num}")

if __name__ == '__main__':
    process_file('/media/aman/aman/college/sem 6/6-sem/app dev/MAD/CHAPTER7.md', 7)
    process_file('/media/aman/aman/college/sem 6/6-sem/app dev/MAD/CHAPTER8.md', 8)
