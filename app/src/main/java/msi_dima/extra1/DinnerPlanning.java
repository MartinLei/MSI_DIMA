/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package msi_dima.extra1;

import org.chocosolver.solver.Model;
import org.chocosolver.solver.Solver;
import org.chocosolver.solver.variables.BoolVar;

import static org.chocosolver.solver.constraints.nary.cnf.LogOp.*;

public class DinnerPlanning {

    /**
     * The CSP:
     * "The Dupont family will visit us tonight," Mr. Martin announces. "The whole family, that is, Mr. and
     * Mrs. Dupont and their three children Emma, Georg and Ivana?" Mrs. Martin asks in dismay.
     * Mr. Martin replies: "That's the problem: they wanted to make a secret about who exactly wants to come.
     * But we know: If Mr. Dupont comes, then his wife will come, too.
     * At least one of the two children Ivana and Georg will come. Either Mrs. Dupont or Emma will come.
     * Either Emma and Georg come both, or they both don't come. And if Ivana comes, then also Georg and
     * Mr. Dupont will come."
     * <p>
     * Help the Martins with the dinner planning: Who will visit the Martins tonight?
     */
    public static void main(String[] args) {
        Model model = new Model("dinner planning");

        // - variables -
        // "The whole family, that is, Mr. and Mrs. Dupont and their three children Emma, Georg and Ivana"
        BoolVar mr_dupont = model.boolVar("Mr. Dupont");
        BoolVar mrs_dupont = model.boolVar("Mrs. Dupont");
        BoolVar emma = model.boolVar("Emma");
        BoolVar georg = model.boolVar("Georg");
        BoolVar ivana = model.boolVar("Ivana");

        // - constraints -
        // 1 If Mr. Dupont comes, then his wife will come, too.
        // Mr.Dupont -> Mrs.Dupont
        model.addClauses(implies(mr_dupont, mrs_dupont));

        // 2. At least one of the two children Ivana and Georg will come.
        // Ivana or Georg
        model.addClauses(or(ivana, georg));

        // 3. Either Mrs. Dupont or Emma will come.
        // Mrs. Dupont xor Emma
        model.addClauses(xor(mrs_dupont, emma));

        // 4. Either Emma and Georg come both, or they both don't come.
        // Emma and Georg or not Emma and not Georg
        model.addClauses(or(and(emma, georg), and(emma.not(), georg.not())));

        // 5. And if Ivana comes, then also Georg and Mr. Dupont will come.
        // Ivana -> Georg and Mr. Dupont
        model.addClauses(implies(ivana, and(georg, mr_dupont)));

        // - solution -
        Solver solver = model.getSolver();
        solver.solve();
        System.out.println("Who will visit the Martins tonight?:");
        System.out.println(mr_dupont);
        System.out.println(mrs_dupont);
        System.out.println(emma);
        System.out.println(ivana);
        System.out.println(georg);

    }
}
