import myTools.BinaryTree;

public class a_stack {
    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree();
        // 해당 트리는 교재 130페이지에서 확인 가능
        tree.push(6);tree.push(4);tree.push(8);tree.push(2);
        tree.push(5);tree.push(7);tree.push(1);tree.push(3);

        System.out.print("In-order : "); tree.show(0);
        System.out.print("Pre-order : "); tree.show(1);
        System.out.print("Post-order : "); tree.show(-1);
    }
}