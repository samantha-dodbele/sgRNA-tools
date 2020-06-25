# F and R Primers Functions
# Original Name "ReverseComplementFunctions"

#Make the inputted string into a list
def strg_to_lst(strg):
    new_lst=[]
    for char in strg:
        new_lst.append(char)
    return new_lst


#Convert list to string
def lst_to_strg(lst):
    new_strg=''
    new_strg= new_strg.join(lst)
    return new_strg


#Generate reverse complement of seq_list
#input list
#output list
def reverse_complement(dna):

#first find complement
    complement = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    complemented_lst = [complement[base] for base in dna]
    
# then reverse the sequence
    reversed_seq = complemented_lst[::-1] 
    return reversed_seq


#Add "CACCG" to the 5' end of the sequence for the FORWARD PRIMER
def get_fwd_primer(strg):
    five_prime_addition_f="caccg"
    forward_primer=five_prime_addition_f+strg
    return (forward_primer)


#Add "AAAC" to the 5' end of the sequence for the REVERSE PRIMER
#Add "C" to the 3' end of the sequence for the REVERSE PRIMER
def get_rev_primer(strg):
    five_prime_addition_r="aaac"
    three_prime_addition_r= "c"
    new_lst=strg_to_lst(strg)
    rev_lst=reverse_complement(new_lst)
    rev_strg=lst_to_strg(rev_lst)
    reverse_primer=five_prime_addition_r+rev_strg+three_prime_addition_r
    return (reverse_primer)


# checks to make sure the inputted string only contains uppercase ATGC
# use strg.upper() before checking char
def check_char(strg):
    for letter in strg:
        if letter !="A" and letter !="T" and letter !="G" and letter !="C":
            #print ("You can only input A, T, G, or C")
            return False
        return True


# strips extra spaces from inputted sequence and puts into uppercase
def prep(strg):
    stripped=strg.strip()
    upper_stripped=stripped.upper()
    return upper_stripped
