package eidi2.sose2022.admission_exam.group01;

import java.util.List;
import java.util.LinkedList;

import eidi2.sose2022.admission_exam.group01.util.Tuple;
import eidi2.sose2022.admission_exam.storage.IStoreable;
import eidi2.sose2022.admission_exam.storage.Vault;

public class VaultingManager {
	final List<Tuple<Bank, List<Vault<IStoreable>>>> banksAndVaults = new LinkedList<>();
	
	Tuple<Bank, List<Vault<IStoreable>>> findBankTuple(Bank bankToFind) {
		for(Tuple<Bank, List<Vault<IStoreable>>> tuple : banksAndVaults) {
			if(tuple.first.equals(bankToFind)) {
				return tuple;
			}
		}
		return null;
	}
	
	/**
	 * adds a Vault to the list of vaults associated with a bank
	 * @param bank for which to add the vault
	 * @param vaultToAdd
	 */
	public void addVaultForBank(Bank bank, Vault<IStoreable> vaultToAdd) {
		if(bank == null || vaultToAdd == null) {
			throw new IllegalArgumentException("Neither Bank nor vaultToAdd can be null!");
		}
			
		var bankTuple = findBankTuple(bank);
		
		if(bankTuple == null) {
			bankTuple = new Tuple<>(bank, new LinkedList<Vault<IStoreable>>());
			banksAndVaults.add(bankTuple);
		}
		bankTuple.second.add(vaultToAdd);
	}
	
	public boolean removeValueFromBankVault(Bank bankToFind, long vaultID, int valueToRemove) {
		Tuple<Bank, List<Vault<IStoreable>>> tuple = findBankTuple(bankToFind);
		if(tuple == null) {return false;}

		Vault<IStoreable> searched_vault = null;
		for(Vault<IStoreable> vault : tuple.second) {
			if (vault.getID() == vaultID){
				searched_vault = vault;
				break;
			}
		}
		if(searched_vault == null) {return false;}

		int val_before_deletion = searched_vault.getValue();
		if(val_before_deletion == searched_vault.removeValue(valueToRemove)) {return false;}

		return true;
	}
	
}
